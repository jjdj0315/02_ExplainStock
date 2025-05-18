import meilisearch
import pandas as pd

client = meilisearch.Client("http://localhost:7700", "aSampleMasterKey")


def stock_search(query):
    return client.index("stocks").search(query)
