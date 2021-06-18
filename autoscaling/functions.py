from aws_client import get_autoscaling, get_ec2
from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from autoscaling.groups import AutoScalingGroup
from models.ScrapingCapacity import ScrapingCapacity
import boto3
from config import AUTO_SCALING_GROUPS, aws_access_key_id, aws_secret_access_key


def create_ec2_instance(autoscaling_group, instances_count, spot=True):
    """ Creates EC2 instances and returns their IDs once all of them are available """
    ec2_client = get_ec2()

    instances = ec2_client.create_instances(
        ImageId='ami-0bb702314608cfd5c', MinCount=1, MaxCount=5)

    autoscaling_client = get_autoscaling()

    autoscaling_client.attach_instances(instances)


def get_ec2_instances(autoscaling_group):
    """ Retrieves EC2 instances from distribution group """

    asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name='eu-west-3')

    asg_response = asg_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[autoscaling_group])

    instance_ids = []  # List to hold the instance-ids

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            instance_ids.append(k['InstanceId'])

    return instance_ids


def launch_ec2_instance():
    pass


def get_live_instances(autoscaling_group):
    """ Retrieves the amount of distributions """

    asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name='eu-west-3')

    asg_response = asg_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[autoscaling_group])

    instance_ids = []  # List to hold the instance-ids

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            instance_ids.append(k['InstanceId'])

    # ec2_response = ec2_client.describe_instances(
    #     InstanceIds=instance_ids
    # )

    instances_count = len(instance_ids)

    # print(instance_ids)  # This line will print the instance_ids

    # Only cycle through one autoscaling group, for now
    # TODO: Implement logic to handle discrepancies in instances count between the different autoscaling groups
    return instances_count


def get_instances_capacity_target(autoscaling_group):
    """ Retrieves the amount of distributions """

    asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name='eu-west-3')

    asg_response = asg_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[autoscaling_group])

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            return i['DesiredCapacity']


def set_capacity(scaling_instructions: CapacityScalingInstructions):

    #instances = get_live_instances(scaling_instructions.autoscaling_group)

    current_instances_target = get_instances_capacity_target(
        scaling_instructions.autoscaling_group)

    print(f'Current desired capacity: {current_instances_target}')

    autoscaling_client = get_autoscaling()

    result = autoscaling_client.update_auto_scaling_group(
        AutoScalingGroupName=scaling_instructions.autoscaling_group,
        DesiredCapacity=scaling_instructions.capacity
    )

    print(result)
