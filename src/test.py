from redis_cluster import RedisCluster
from redis_cluster.functions import get_capacity
from lambda_handler import lambda_function
from models.CrawlerThreadsPool import CrawlerThreadsPool
from multiprocessing import Process
import random
import string
import requests

print(
    RedisCluster.get_connection().execute_command("KEYS *")
)

# data = {
#     "crawler_threads": {
#         "crawler_engines": {
#             "SPIDER": 2938,
#             "SCRAPER": 2938
#         },
#         "total": 10239
#     }
# }


# lambda_function(data, None)

# def a(pool: CrawlerThreadsPool):
#     domains = []
#     for i in range(99):
#         domains.append(
#             ''.join(random.choice(string.ascii_uppercase + string.digits)
#                     for _ in range(10))
#         )

#     crawler_engines = ['SCRAPER', 'DOMAIN']

#     while True:
#         crawler_engine = random.choice(crawler_engines)
#         domain = random.choice(domains)

#         val = ''.join(random.choice(string.ascii_uppercase + string.digits)
#                       for _ in range(10))

#         pool.add({
#             'crawler_engine': crawler_engine,
#             'domain': domain,
#             'thread_id': val,
#         })


# obj = CrawlerThreadsPool()

# process = Process(target=a, args=(obj,))


# process.start()


# while True:
#     pass
# cp = obj.distinct_domains.copy()

# print('Tot items: %d, Unique domains: %d/%d, Unique crawler_engine: %d' % (
#     obj.pool.qsize(),
#     len(cp.keys()),
#     sum(
#         [len(cp[dom]) for dom in cp]
#     ),
#     len(obj.distinct_crawler_engines.keys()),

# ))
