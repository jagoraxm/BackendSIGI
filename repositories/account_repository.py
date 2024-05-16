import decimal
import oracledb
from datetime import datetime, timedelta
from typing import Tuple

# connection database
from database.oracle.connection import connection
# Schemas
from schemas.account_schema import AccountStatus
# services
from services.logger_service import logger
from services.set_responses_service import error_response


def account_status_ula(student_enrollment_number: str) -> list[AccountStatus]:
    """
    This function to use banner stored function 'pkg_finanzas_ula.f_estado_cuenta_espacio'
    """
    logger.debug(f"account_status_ula() accessed")
    logger.debug(f"The incoming registration is: {student_enrollment_number}")

    # connection database oracle
    conec = connection()

    try:
        # cursor initialization
        cursor = conec.cursor()
        # context switch
        cursor.callproc("CONTEXTO.Empresa", ["ULA"])
        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored procedure CALL CONTEXTO called successfully")

        cursor_data = cursor.callfunc(
            "BANINST1.pkg_finanzas_ula.f_estado_cuenta_espacio",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number]
        )
        data = cursor_data.fetchall()

        records_list: list[AccountStatus] = []

        for col in data:
            record = AccountStatus(
                trans_cargo=col[0],
                periodo_cargo=col[1],
                mes=col[2],
                desc_concepto_cargo=col[3],
                importe=col[4],
                beca=col[5],
                pagos=col[6],
                becas=col[7],
                cargos=col[8],
                saldo_final=col[9],
                fecha_vencimiento_cargo=col[10],
                saldo_pendiente=col[11],
                tipo=col[12],
                iden=col[13],
                nombre=col[14],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.f_estado_cuenta_espacio called successfully")

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

    records_list = [account_status.dict() for account_status in records_list]
    return records_list


def account_status_utc(student_enrollment_number: str) -> list[AccountStatus]:
    """
    This function to use banner stored function 'pkg_finanzas_utc.f_estado_cuenta_espacio'
    """
    logger.debug(f"account_status_utc() accessed")

    # connection database oracle
    conec = connection()

    try:
        # cursor initialization
        cursor = conec.cursor()
        # context switch
        cursor.callproc("CONTEXTO.Empresa", ["UTC"])
        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored procedure CALL CONTEXTO called successfully")

        cursor_data = cursor.callfunc(
            "BANINST1.pkg_finanzas_utc.f_estado_cuenta_espacio",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number]
        )
        data = cursor_data.fetchall()

        records_list: list[AccountStatus] = []

        for col in data:
            record = AccountStatus(
                trans_cargo=col[0],
                periodo_cargo=col[1],
                mes=col[2],
                desc_concepto_cargo=col[3],
                importe=col[4],
                beca=col[5],
                pagos=col[6],
                becas=col[7],
                cargos=col[8],
                saldo_final=col[9],
                fecha_vencimiento_cargo=col[10],
                saldo_pendiente=col[11],
                tipo=col[12],
                iden=col[13],
                nombre=col[14],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.f_estado_cuenta_espacio called successfully")

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

    records_list = [account_status.dict() for account_status in records_list]
    return records_list
