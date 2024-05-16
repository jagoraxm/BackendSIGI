import decimal
import oracledb
from datetime import datetime, timedelta
from typing import Tuple, Dict, Any

# connection database
from database.oracle.connection2 import connection2
# Schemas
from schemas.payment_schema import Debts, Sequence, Reference, GenerateSheet
# services
from schemas.student_schema import GeneralData
from services.logger_service import logger
from services.set_responses_service import error_response


def general_data_utg(student_enrollment_number: str) -> list[GeneralData]:
    """
    This function to use banner stored function 'pkg_espacio_uteg.f_datos_gral'
    """
    logger.debug(f"general_data_utg() accessed")
    logger.debug(f"The incoming registration is: {student_enrollment_number}")

    # connection database oracle
    conec = connection2()

    try:
        # cursor initialization
        cursor = conec.cursor()
        # context switch
        cursor.callproc("CONTEXTO.Empresa", ["UTG"])
        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored procedure CALL CONTEXTO called successfully")

        cursor_data = cursor.callfunc(
            "BANINST1.pkg_espacio_uteg.f_datos_gral",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number]
        )
        data = cursor_data.fetchall()

        records_list: list[GeneralData] = []

        for col in data:
            record = GeneralData(
                matricula=col[0],
                nombre=col[1],
                campus=col[2],
                nivel=col[3],
                clave_prog=col[4],
                programa=col[5],
                turno=col[6],
                grupo=col[7],
                celular=col[8],
                incorporante=col[9],
                cred_cursados=col[10],
                cred_prog=col[11],
                periodicidad=col[12],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_espacio_uteg.f_datos_gral called successfully")


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

    records_list = [general_data.dict() for general_data in records_list]
    return records_list
