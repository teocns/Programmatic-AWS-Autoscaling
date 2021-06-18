class DistributionInstance:
    name: str
    count: int

    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count
