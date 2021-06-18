from models.ScrapingCapacity import ScrapingCapacity
from autoscaling.ScrapingCapacity import ScrapingCapacity
from autoscaling.functions import get_required_scraping_capacity, get_current_scraping_capacity, set_autoscaling_capacity
from aws_client import get_distributions_count
from config import CAPACITY_PER_DISTRIBUTION
import boto3


# Get amount of distributions


def lambda_function():
    # distributions_count = get_distributions_count()
    # current_scraping_capacity = distributions_count * CAPACITY_PER_DISTRIBUTION

    current_capacity: ScrapingCapacity = get_current_scraping_capacity()

    required_capacity: ScrapingCapacity = get_required_scraping_capacity()

    print(
        f'Current scraping capcity: SCRAPER({current_capacity.scraper}) | SPIDER({current_capacity.spider}) ')

    print(
        f'Required capacity: SCRAPER({required_capacity.scraper}) | SPIDER({required_capacity.spider})')

    # Adjust capacity for SCRAPER
    current_scraper_distributions = int(
        current_capacity.scraper / CAPACITY_PER_DISTRIBUTION)
    required_scraper_distributions = int(
        required_capacity.scraper / CAPACITY_PER_DISTRIBUTION)

    if required_capacity.scraper < current_capacity.scraper:
        # SCALE DOWN
        # Assert that we can scale down
        if current_scraper_distributions <= 1 or required_scraper_distributions == current_scraper_distributions:
            print('No action should be taken')
            return
        
    elif required_capacity.scraper > current_capacity.scraper:
        # SCALE UP
        # Assert that we can perform down-scale

        if current_scraper_distributions < required_scraper_distributions:
            print(
                f'Scaling SCRAPER capacity from {current_scraper_distributions} to {required_scraper_distributions}')
            return
        print('No action should be taken')


lambda_function()
