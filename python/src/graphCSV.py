from pymongo import MongoClient
from python.graphs.graph import svoGraphCSV
import config


if __name__ == '__main__':
    client = MongoClient(config.db_clientTopic)
    database = client[config.db_users]
    collection = database[config.db_collectionUsersSVO]

    svoGraphCSV(collection, config.svoGraphFilename)
