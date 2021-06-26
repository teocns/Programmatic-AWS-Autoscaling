from autoscaling.ScrapingCapacity import AutoscalingDistributionsCapacity
from redis_cluster import RedisCluster


def get_capacity()-> AutoscalingDistributionsCapacity:
    conn = RedisCluster.get_connection()
    capacity = conn.hgetall('CRAWLING_CAPACITY_FORECAST')
    spider=int(capacity.get('SPIDER') or 0)
    scraper=int(capacity.get('SCRAPER') or 0)
    return AutoscalingDistributionsCapacity(
        spider=spider,
        scraper=scraper,
        processor=spider+scraper
    )
    