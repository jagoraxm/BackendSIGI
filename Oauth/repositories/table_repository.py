# modules
import oracledb
from pydantic import ValidationError, parse_obj_as

#  database
from database.oracle.connection import connection

# services
from services.logger_service import logger
from services.set_responses_service import error_response


def find_all(student_id: int, school: str):
    """
    This function get data transaction of banner
    """
    logger.debug(f"find_all() accessed - student_id: {student_id}")

    global cursor, conec

    # connection database oracle
    conec = connection()

    try:
        cursor = conec.cursor()
        cursor.callproc("CONTEXTO.Empresa", [school])

        # Define the procedure call
        query = f"""
           SELECT * FROM TBRACCD WHERE TBRACCD_PIDM = '{student_id}'
        """

        # Execute the procedure call
        try:
            # Execute the procedure call
            cursor.execute(query)
        except oracledb.IntegrityError as e:
            error_obj = e.args
            logger.error("Transaction Details Repository - find_one() - IntegrityError")
            logger.error(f"Error Message: {error_obj.message}")
            return error_response(503, f"{e}", f"An error occurred while executing query: {e}"), 503

        result = cursor.fetchone()
        print(result)
    except oracledb.DatabaseError as e:
        logger.error(f"An error occurred while executing query: {e}")
        return error_response(503, f"{e}", f"An error occurred while executing query: {e}"), 503

    except Exception as e:
        logger.error(f"An error occurred {e}")
        return error_response(503, f"{e}", f"An error occurred: {e}"), 503

    finally:
        # Close the cursor and connection
        cursor.close()
        conec.close()
