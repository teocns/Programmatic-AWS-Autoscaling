class ScrapingCapacity:
    spider: int
    scraper: int

    def __init__(self, scraper=0, spider=0) -> None:
        self.spider = spider
        self.scraper = scraper
