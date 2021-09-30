"""
Log carbon usage
"""
import logging
import time

from .carbon_intensity import get_intensity


def log_intensity(function, *args, **kwargs):
    start_time = time.time()
    start_intensity = get_intensity()

    output = function(*args, **kwargs)

    end_time = time.time()

    logging.info(f"Took {end_time - start_time}s at {start_intensity} carbon intensity")
