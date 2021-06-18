class ScrapingCapacity:
    spider: int
    scraper: int

    def __init__(self, scraper, spider) -> None:
        self.spider = spider
        self.scraper = scraper
