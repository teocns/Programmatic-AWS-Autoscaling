
from aws_client import get_dynamodb
from config import CAPACITY_PER_DISTRIBUTION, DOMAIN_RATE_LIMIT
from aws_client import get_distributions_count


def get_scraping_capacity_required():

    # Get all crawler threads that need to be processed
    dynamo = get_dynamodb()

    table = dynamo.Table('crawler_threads')

    data = table.query(
        IndexName='is_completed-index',
        KeyConditionExpression="#is_completed = :is_completed",
        ExpressionAttributeNames={
            "#is_completed": "is_completed"
        },
        ExpressionAttributeValues={
            ":is_completed": 0
        }

    )

    total_capacity_required = 0

    # domain: count
    per_domain_capacity = {

    }

    for x in data['Items']:
        domain = x['domain']

        if not domain in per_domain_capacity:
            per_domain_capacity[domain] = 1
            total_capacity_required += 1
            continue

        current_val = per_domain_capacity[domain]
        if current_val >= DOMAIN_RATE_LIMIT:
            # Domain already saturated
            continue

        per_domain_capacity[domain] += 1
        total_capacity_required += 1

    return total_capacity_required


def scale_up(is_completed):
    # Scale up both crawler_environment, rate_limiter and processor
    pass


def get_scraping_capacity():
    return get_distributions_count() * CAPACITY_PER_DISTRIBUTION


get_scraping_capacity_required()
