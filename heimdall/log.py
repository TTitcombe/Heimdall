"""
Log carbon usage
"""
import logging
import time

from pymongo import MongoClient

from .carbon_intensity import get_carbon_intensity


def log_intensity(function, *args, **kwargs):
    start_time = time.time()
    start_intensity = get_carbon_intensity()

    output = function(*args, **kwargs)

    end_time = time.time()

    logging.info(f"Took {end_time - start_time}s at {start_intensity} carbon intensity")


def log_intensity_mongo(mongo_client: MongoClient, database, collection):
    def outer_wrap(func):
        def inner_wrap(*args, **kwargs):
            start_time = time.time()
            start_intensity = get_carbon_intensity()

            output = func(*args, **kwargs)
            end_time = time.time()

            db_col = mongo_client[database][collection]
            db_col.insert_one(
                {
                    "execution time": end_time - start_time,
                    "carbon intensity": start_intensity
                }
            )

            return output
        return inner_wrap
    return outer_wrap
    