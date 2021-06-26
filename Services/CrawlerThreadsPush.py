import this
from multiprocessing.queues import Queue
from multiprocessing import Process, Manager


class CrawlerThreadsPush:
    """ Aggregate CrawkerThreads ready to be sent to processing"""

    crawler_threads: dict

    # We store thread ID for each of the following

    crawler_engine_to_thread_id: dict
    domain_to_thread_id: dict

    @staticmethod
    def run(crawler_threads_queue: Queue):

        # Start in an isolated Process to spread load
        # Pass the Queue directly to the constructor to ensure object sharing
        process = Process(target=CrawlerThreadsPush.crawler_threads,
                          args=(crawler_threads_queue,))

        process.start()

        return crawler_threads_queue

    def __init__(self, crawler_threads_queue) -> None:
        capcity =
        while True:

            pass
