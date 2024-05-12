# modules
import oracledb

# constants
from config import Settings

# services
from services.logger_service import logger
from services.set_responses_service import error_response


config = Settings()


def connection():
    """
        This function makes the connection to oracleDB version Oracle Database 18c Enterprise
        Edition Release 18.0.0.0.0 - Production,  Oracle JDBC driver 12.2.0.1.0
        :return: the connection
    """
    logger.debug("connection() accessed")
    try:
        # Create connection to Oracle database
        connection_db = oracledb.connect(user=config.banner_9_db_user, password=config.banner_9_db_password,
                                          dsn=config.dsn, encoding=config.encoding)
        logger.debug(connection_db)
        logger.debug(f"version of connection: {connection_db.version}.")
        logger.debug("Connection to Oracle DB successfully")
        return connection_db

    except oracledb.OperationalError as e:
        logger.debug(f"There was an error connecting to the Oracle database or VPN interconnection error : {e}")
        return error_response(503, f"There was an error connecting to the Oracle database "
                                   f"or VPN interconnection error: {e}",
                              f"There was an error connecting to the Oracle database "
                              f"or VPN interconnection error: {e}"), 503

    except oracledb.DatabaseError as e:
        logger.debug(f"There was an error of connecting  to Oracle database: {e}")
        return error_response(503, f"There was an error of connecting to Oracle database: {e}",
                              f"There was an error of connecting to Oracle database: {e}"), 503





