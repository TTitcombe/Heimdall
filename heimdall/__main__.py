from pymongo import MongoClient

from .log import log_intensity_mongo

client = MongoClient("localhost", 27017)


log_intensity_mongo(client, "test_db", "carbon")
def test_function():
    for i in range(100_000):
        print(i**3)


test_function()
