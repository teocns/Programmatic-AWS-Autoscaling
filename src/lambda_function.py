from redis_cluster.functions import get_capacity
from functions import get_scaling_instructions_for_processor, get_scaling_instructions_for_scraper, get_scaling_instructions_for_spider
from autoscaling.groups import AutoScalingGroup
from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from autoscaling.ScrapingCapacity import AutoscalingDistributionsCapacity
from autoscaling.functions import  get_current_distributions_capacity, set_autoscaling_desired_distributions_capacity
import boto3


def lambda_handler(context, event):
    # View sample_event.json for the content of "context"


    required_scraping_capacity = get_capacity()

    
    current_scraping_capacity: AutoscalingDistributionsCapacity = get_current_distributions_capacity()

    
    print(
        f'Current scraping capcity: SCRAPER({current_scraping_capacity.scraper}) | SPIDER({current_scraping_capacity.spider}) | PROCESSOR({current_scraping_capacity.processor})')

    print(
        f'Required capacity: SCRAPER({required_scraping_capacity.scraper}) | SPIDER({required_scraping_capacity.spider})')

    scaling_instructions_scraper = get_scaling_instructions_for_scraper(
        current_scraping_capacity, required_scraping_capacity)

    scaling_instructions_spider = get_scaling_instructions_for_spider(
        current_scraping_capacity, required_scraping_capacity)

    scaling_instructions_processor = get_scaling_instructions_for_processor(
        current_scraping_capacity, required_scraping_capacity)

    # Scale scraper
    if scaling_instructions_scraper:
        set_autoscaling_desired_distributions_capacity(
            AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.SCRAPER),
            scaling_instructions_scraper)

    if scaling_instructions_spider:
        set_autoscaling_desired_distributions_capacity(
            AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.SPIDER),
            scaling_instructions_spider)

    if scaling_instructions_processor:
        set_autoscaling_desired_distributions_capacity(
            AutoScalingGroup.get_auto_scaling_group_codename(AutoScalingGroup.PROCESSOR),
            scaling_instructions_processor)



