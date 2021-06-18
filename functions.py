
from aws_client import get_dynamodb
from config import CAPACITY_PER_DISTRIBUTION, DOMAIN_RATE_LIMIT
from aws_client import get_distributions_count


def scale_up(is_completed):
    # Scale up both crawler_environment, rate_limiter and processor
    pass


def get_scraping_capacity():
    return get_distributions_count() * CAPACITY_PER_DISTRIBUTION
