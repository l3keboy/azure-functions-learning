from logic import test
import logging


async def add_1_two_times():
    logging.info("Adding 1+1 and 1+1")
    result1 = await test.add_1_1()
    result2 = await test.add_1_1()
    return result1 + result2
