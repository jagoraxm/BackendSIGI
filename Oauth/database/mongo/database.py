import pymongo
import pymongo.errors
from services.loggerService import logger


def connectionDB(url):
    """
      this function makes the connection to MongoDB
      :return: the connection
    """
    # connection basic
    try:
        mongo = pymongo.MongoClient(url)
        logger.debug(f"Connection to: {mongo}.")

        logger.info("Mongodb answered correctly")
        print("Mongodb answered correctly")
        return mongo
    except pymongo.errors.ConnectionFailure as e:
        logger.error(f'Could not connect to server: {e}')
        logger.error("An error occurred while trying to communicate with the mongodb database")
        print("An error occurred while trying to communicate with the mongodb database")
        return communication_error

