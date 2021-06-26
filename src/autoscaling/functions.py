
from autoscaling.ScrapingCapacity import AutoscalingDistributionsCapacity
from aws_client import get_autoscaling, get_ec2, get_dynamodb

from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from autoscaling.groups import AutoScalingGroup

import boto3
from config import AUTO_SCALING_GROUPS, CAPACITY_PER_DISTRIBUTION, aws_access_key_id, aws_secret_access_key


def get_current_distributions_capacity():

    capacity = AutoscalingDistributionsCapacity()

    capacity.scraper = get_autoscaling_desired_distributions_capacity(
        AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.SCRAPER)
    ) * CAPACITY_PER_DISTRIBUTION

    capacity.spider = get_autoscaling_desired_distributions_capacity(
        AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.SPIDER)
    ) * CAPACITY_PER_DISTRIBUTION

    capacity.processor = get_autoscaling_desired_distributions_capacity(
        AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.PROCESSOR)
    ) * CAPACITY_PER_DISTRIBUTION
    return capacity



def get_autoscaling_desired_distributions_capacity(autoscaling_group):
    """ Retrieves the amount of distributions """

    asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name='eu-west-3')

    asg_response = asg_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[autoscaling_group])

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            return i['DesiredCapacity']


def set_autoscaling_desired_distributions_capacity(autoscaling_group_aws_codename, capacity: CapacityScalingInstructions):

    print(
        f'Changing EC2 DesiredCapacity to [{capacity.distributions}] for [{autoscaling_group_aws_codename}]')
    autoscaling_client = get_autoscaling()

    result = autoscaling_client.update_auto_scaling_group(
        AutoScalingGroupName=autoscaling_group_aws_codename,
        DesiredCapacity=capacity.distributions
    )

    print(result)

