import decimal
import oracledb
from datetime import datetime, timedelta
from typing import Tuple, Dict, Any

# connection database
from database.oracle.connection2 import connection2
# Schemas
from schemas.payment_schema import Debts, Sequence, Reference, GenerateSheet, PaymentSheet
# services
from services.logger_service import logger
from services.set_responses_service import error_response


def debts_utg(student_enrollment_number: str) -> list[Debts]:
    """
    This function to use banner stored function 'PKG_REFERENCIAS_UTG.F_ADEUDOS'
    """
    logger.debug(f"debts_utg() accessed")
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
            "BANINST1.pkg_referencias_utg.f_adeudos",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number]
        )
        data = cursor_data.fetchall()

        records_list: list[Debts] = []

        for col in data:
            record = Debts(
                periodo=col[0],
                periodo_desc=col[1],
                transaccion=col[2],
                cod_det=col[3],
                descripcion=col[4],
                importe=col[5],
                descuentos=col[6],
                pagos_aplicados=col[7],
                saldo=col[8],
                fecha_venc=col[9],
                ficha=col[10],
                pagos_sin_aplicar=col[11],
                tipo_concepto=col[12],
                desc_pago_com=col[13],
                desc_pronto_pago=col[14],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_referencias_utg.f_adeudos called successfully")

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

    records_list = [debts.dict() for debts in records_list]
    return records_list


def sequence_utg() -> int:
    """
    This function to use banner stored function 'PKG_REFERENCIAS_UTG.F_ADEUDOS'
    """
    logger.debug(f"sequence_utg() accessed")

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

        data = cursor.callfunc(
            "pkg_referencias_utg.f_retorna_secuencia",
            oracledb.DB_TYPE_NUMBER
        )
        sequence_number = Sequence(
            sequence=data
        )
        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_referencias_utg.f_retorna_secuencia called successfully: {}")

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

    return sequence_number.sequence


def insert_bank_utg(student_enrollment_number: str, sequence_number: int,
                    transaction_number: str, amount: float, pc: int) -> int:
    """
    This function to use banner stored function 'pkg_referencias_utg.f_insert_tzdbank'
    """
    logger.debug(f"insert_bank_utg() accessed")
    logger.debug(f"The incoming registration are: {student_enrollment_number}, "
                 f"{sequence_number}, {transaction_number}, {amount}, {pc}")

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

        result_data = cursor.callfunc(
            "BANINST1.pkg_referencias_utg.f_insert_tzdbank",
            oracledb.STRING,
            [student_enrollment_number, sequence_number,
             transaction_number, amount, pc]
        )
        logger.debug(f"The result_data is: {result_data}")
        insertion_flag = int(result_data)
        if insertion_flag == 1:
            logger.debug(f"The following data has been inserted correctly: "
                         f"student_enrollment_number:{student_enrollment_number}, "
                         f"sequence_number: {sequence_number}, "
                         f"transaction_number: {transaction_number}, "
                         f"amount: {amount}, "
                         f"pc: {pc}")
        elif insertion_flag == 0:
            logger.error(f"An error occurred: Data could not be inserted  into the database")

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_referencias_utg.f_insert_tzdbank called successfully")

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

    return insertion_flag


def generate_sheet_utg(student_enrollment_number: str, sequence_number: int) -> list:
    """
    This function to use banner stored function 'pkg_referencias_utg.Genera_Ficha'
    """
    logger.debug(f"reference_utg() accessed")
    logger.debug(f"The incoming registration are: {student_enrollment_number, sequence_number}")

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

        # Execute the procedure call
        result = cursor.callproc("BANINST1.pkg_referencias_utg.Genera_Ficha", [student_enrollment_number,
                                                                               sequence_number])
        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("The query SELECT * FROM TZRBANK WHERE TZRBANK_REF_NUMBER was executed correctly")

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

    return result


def reference_utg(sequence_number: int) -> dict:
    """
    This function to use 'SELECT * FROM TZRBANK'
    """
    logger.debug(f"reference_utg() accessed")
    logger.debug(f"The incoming registration are: {sequence_number}")

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

        query = "SELECT * FROM TZRBANK WHERE TZRBANK_REF_NUMBER = :sequence_number"
        cursor.execute(query, sequence_number=sequence_number)
        result = cursor.fetchone()

        references = GenerateSheet(
            pidm=result[0],
            amount=result[1],
            due_date=str(result[2]),
            ref_number=result[3],
            activity_date=result[4],
            status=result[5],
            user=result[6],
            ref_santander=result[7],
            ref_banbajio=result[8],
            ref_oxxo=result[9],
            add=result[10],
            add_one=result[11],
            add_two=result[12],
            add_three=result[12]
        )

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("The query SELECT * FROM TZRBANK WHERE TZRBANK_REF_NUMBER was executed correctly")

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

    return references.dict()


def list_payment_sheet_utg(student_enrollment_number: str) -> list[PaymentSheet]:
    """
    This function to use 'pkg_referencias_utg.f_retorna_tzrbank('
    """
    logger.debug(f"list_payment_sheet_utg() accessed")
    logger.debug(f"The incoming registration are: {student_enrollment_number}")

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
            "BANINST1.pkg_referencias_utg.f_retorna_tzrbank",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number]
        )
        data = cursor_data.fetchall()

        records_list: list[PaymentSheet] = []

        for col in data:
            record = PaymentSheet(
                secuencia=col[0],
                monto=col[1],
                fecha_vencimiento=col[2],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_referencias_utg.f_retorna_tzrbank called successfully")

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

    records_list = [payment_sheet.dict() for payment_sheet in records_list]
    return records_list
