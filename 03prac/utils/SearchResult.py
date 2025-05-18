class SearchResult:
    def __init__(self, item):
        self.item = item

    @property
    def symbol(self):
        return self.item["Symbol"]

    @property
    def name(self):
        return self.item["Name"]

    def __str__(self):
        return f"{self.symbol}: {self.name}"