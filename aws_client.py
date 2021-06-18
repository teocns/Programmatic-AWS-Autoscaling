from typing import List
import boto3
from config import AUTO_SCALING_GROUPS, aws_access_key_id, aws_secret_access_key
from queue import Queue
import time


def get_dynamodb():
    return boto3.resource('dynamodb', region_name="eu-west-3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


def get_autoscaling():
    return boto3.client('autoscaling', region_name="eu-west-3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


def get_ec2():
    return boto3.client('autoscaling', region_name="eu-west-3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


def get_distributions_count():
    """ Retrieves the amount of distributions """

    # autoscaling = get_autoscaling()

    # groups = autoscaling.describe_auto_scaling_groups()['AutoScalingGroups']

    # print(groups[0])

    # pass

    asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name='eu-west-3')

    for auto_scaling_group_name in AUTO_SCALING_GROUPS:

        asg_response = asg_client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[auto_scaling_group_name])

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
        break


get_distributions_count()
