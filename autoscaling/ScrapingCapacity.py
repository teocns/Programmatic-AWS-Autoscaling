class AutoscalingDistributionsCapacity:
    spider: int
    scraper: int
    processor: int

    def __init__(self, scraper=0, spider=0, processor=0) -> None:
        self.spider = spider
        self.scraper = scraper
        self.processor = processor
