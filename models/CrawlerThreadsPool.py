from multiprocessing import Pool, Queue
from custom_types.dictarray import dictarray
from multiprocessing import Manager


class CrawlerThreadsPool(object):

    pool: Queue

    # Dictionary
    distinct_domains: dictarray
    distinct_crawler_engines: dictarray

    def __init__(self) -> None:
        m = Manager()
        self.pool = Queue()
        self.distinct_domains = m.dict()
        self.distinct_crawler_engines = m.dict()

    def add(self, crawler_thread: dict):
        self.pool.put(crawler_thread)

        thread_id = crawler_thread.get('thread_id')
        domain = crawler_thread.get('domain')
        crawler_engine = crawler_thread.get('crawler_engine')

        if not domain in self.distinct_domains:
            self.distinct_domains[domain] = [thread_id]
        else:
            self.distinct_domains[domain].append(thread_id)

        if not crawler_engine in self.distinct_crawler_engines:
            self.distinct_crawler_engines[crawler_engine] = [thread_id]
        else:
            self.distinct_crawler_engines[crawler_engine].append(
                thread_id)

        pass

    def remove(crawler_thread_id):
        pass

    pass
