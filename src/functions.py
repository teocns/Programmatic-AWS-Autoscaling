
from autoscaling.ScrapingCapacity import AutoscalingDistributionsCapacity
from autoscaling.groups import AutoScalingGroup
from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from aws_client import get_dynamodb
from config import CAPACITY_PER_DISTRIBUTION
#from aws_client import get_distributions_count


def scale_up(is_completed):
    # Scale up both crawler_environment, rate_limiter and processor
    pass


# def get_scraping_capacity():
#     return get_distributions_count() * CAPACITY_PER_DISTRIBUTION


def get_scaling_instructions_for_scraper(current_capacity, required_capacity):
    # Adjust capacity for SCRAPER
    current_scraper_distributions = int(
        current_capacity.scraper / CAPACITY_PER_DISTRIBUTION)
    required_scraper_distributions = int(
        required_capacity.scraper / CAPACITY_PER_DISTRIBUTION)
    if required_scraper_distributions < 1:
        required_scraper_distributions = 1

    if required_capacity.scraper < current_capacity.scraper:
        # SCALE DOWN
        # Assert that we can scale down
        if current_scraper_distributions <= 1 or required_scraper_distributions == current_scraper_distributions:
            print('No action should be taken')
            return None

        return CapacityScalingInstructions(
            autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                AutoScalingGroup.SCRAPER
            ),
            distributions=required_scraper_distributions
        )

    elif required_capacity.scraper > current_capacity.scraper:
        # SCALE UP
        # Assert that we can perform down-scale

        if current_scraper_distributions < required_scraper_distributions:
            print(
                f'Scaling SCRAPER capacity from {current_scraper_distributions} to {required_scraper_distributions}')
            return CapacityScalingInstructions(
                autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                    AutoScalingGroup.SCRAPER
                ),
                distributions=required_scraper_distributions
            )
        print('No action should be taken')


def get_scaling_instructions_for_spider(current_capacity, required_capacity):
    # Adjust capacity for SCRAPER
    current_scraper_distributions = int(
        current_capacity.spider / CAPACITY_PER_DISTRIBUTION)
    required_scraper_distributions = int(
        required_capacity.spider / CAPACITY_PER_DISTRIBUTION)

    if required_scraper_distributions < 1:
        required_scraper_distributions = 1
    if required_capacity.spider < current_capacity.spider:  
        # SCALE DOWN
        # Assert that we can scale down
        if current_scraper_distributions <= 1 or required_scraper_distributions == current_scraper_distributions:
            return None

        return CapacityScalingInstructions(
            autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                AutoScalingGroup.SPIDER
            ),
            distributions=required_scraper_distributions
        )

    elif required_capacity.spider > current_capacity.spider:
        # SCALE UP
        # Assert that we can perform down-scale

        if current_scraper_distributions < required_scraper_distributions:
            print(
                f'Scaling SCRAPER capacity from {current_scraper_distributions} to {required_scraper_distributions}')
            return CapacityScalingInstructions(
                autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                    AutoScalingGroup.SPIDER
                ),
                distributions=required_scraper_distributions
            )


def get_scaling_instructions_for_processor(current_capacity: AutoscalingDistributionsCapacity, required_capacity: AutoscalingDistributionsCapacity):
    # Adjust capacity for SCRAPER
    current_scraper_distributions = int(
        current_capacity.processor / CAPACITY_PER_DISTRIBUTION)
    required_scraper_distributions = int(
        required_capacity.processor / CAPACITY_PER_DISTRIBUTION)


    if required_scraper_distributions < 1:
        required_scraper_distributions = 1
    if required_capacity.processor < current_capacity.processor:
        # SCALE DOWN
        # Assert that we can scale down
        if current_scraper_distributions <= 1 or required_scraper_distributions == current_scraper_distributions:
            return None

        return CapacityScalingInstructions(
            autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                AutoScalingGroup.PROCESSOR
            ),
            distributions=required_scraper_distributions
        )

    elif required_capacity.processor > current_capacity.processor:
        # SCALE UP
        # Assert that we can perform down-scale

        if current_scraper_distributions < required_scraper_distributions:
            print(
                f'Scaling SCRAPER capacity from {current_scraper_distributions} to {required_scraper_distributions}')
            return CapacityScalingInstructions(
                autoscaling_group_aws_codename=AutoScalingGroup.get_auto_scaling_group_codename(
                    AutoScalingGroup.PROCESSOR
                ),
                distributions=required_scraper_distributions
            )
