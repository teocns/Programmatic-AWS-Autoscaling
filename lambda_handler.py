from aws_client import get_distributions_count
from functions import get_scraping_capacity, get_scraping_capacity_required
from config import CAPACITY_PER_DISTRIBUTION
import boto3


# Get amount of distributions


def lambda_function():
    # distributions_count = get_distributions_count()
    # current_scraping_capacity = distributions_count * CAPACITY_PER_DISTRIBUTION

    distributions_count = 4

    current_scraping_capacity = distributions_count * CAPACITY_PER_DISTRIBUTION

    required_capacity = 23092

    print(f'Current scraping capcity: {current_scraping_capacity}')
    print(f'Required capacity: {required_capacity}')

    if required_capacity < current_scraping_capacity:
        # Assert that we can scale down
        current_distributions = int(
            current_scraping_capacity / CAPACITY_PER_DISTRIBUTION)
        if current_distributions <= 1:
            print('No action should be taken')
            return
    elif required_capacity > current_scraping_capacity:
        # Assert that we can scale down

        required_distributions = int(
            required_capacity / CAPACITY_PER_DISTRIBUTION)

        if distributions_count < required_distributions:

            print(
                f'Increasing distirbution capacity from {distributions_count} to {required_distributions}')
            return
        print('No action should be taken')


lambda_function()
