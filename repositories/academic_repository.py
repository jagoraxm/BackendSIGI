import decimal
import oracledb
from datetime import datetime, timedelta
from typing import Tuple

#contants
from constants.constants import ULA, UTC

# connection database
from database.oracle.connection import connection

# Schemas
from schemas.academic_schema import ReportCard, AcademicHistory, ReportCardUnam

# services
from services.logger_service import logger
from services.set_responses_service import error_response


def report_card_ula(period: str, student_enrollment_number: str, program: str) -> list[ReportCard]:
    """
    This function to use banner stored function 'pkg_datos_academicos.f_espacio_boleta_calif_ULA'
    """
    logger.debug(f"report_card_ula() accessed")
    logger.debug(f"The incoming data is: period: {period}, "
                 f"student_enrollment_number: {student_enrollment_number}, "
                 f"program: {program}")

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
            "BANINST1.pkg_datos_academicos.f_espacio_boleta_calif_ULA",
            oracledb.DB_TYPE_CURSOR,
            [period, student_enrollment_number, program]
        )
        data = cursor_data.fetchall()

        records_list: list[ReportCard] = []

        for col in data:
            record = ReportCard(
                crn=col[0],
                matricula=col[1],
                alumno=col[2],
                campus=col[3],
                programa=col[4],
                ciclo=col[5],
                bloque=col[6],
                grupo=col[7],
                num_mat=col[8],
                clave=col[9],
                asignatura=col[10],
                parcial1=col[11],
                parcial2=col[12],
                parcial3=col[13],
                exam_final=col[14],
                prom_p1=col[15],
                prom_p2=col[16],
                prom_p3=col[17],
                prom_exfinal=col[18],
                prom_f=col[19],
                faltasp1=col[20],
                faltasp2=col[21],
                faltasp3=col[22],
                cal=col[23],
                prom_cal=col[24],
                calif_final=col[25]
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_datos_academicos.f_espacio_boleta_calif_ULA "
                     "called successfully")

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

    records_list = [report_card.dict() for report_card in records_list]
    return records_list


def report_card_utc(period: str, student_enrollment_number: str, program: str) -> list[ReportCard]:
    """
    This function to use banner stored function 'pkg_datos_academicos_utc.f_espacio_boleta_calif_UTC'
    """
    logger.debug(f"report_card_utc() accessed")
    logger.debug(f"The incoming data is: period: {period}, "
                 f"student_enrollment_number: {student_enrollment_number}, "
                 f"program: {program}")

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
            "BANINST1.pkg_datos_academicos_utc.f_espacio_boleta_calif_UTC",
            oracledb.DB_TYPE_CURSOR,
            [period, student_enrollment_number, program]
        )

        data = cursor_data.fetchall()

        records_list: list[ReportCard] = []

        for col in data:

            record = ReportCard(
                crn=col[0],
                matricula=col[1],
                alumno=col[2],
                campus=col[3],
                programa=col[4],
                ciclo=col[5],
                bloque=col[6],
                grupo=col[7],
                num_mat=col[8],
                clave=col[9],
                asignatura=col[10],
                parcial1=col[11],
                parcial2=col[12],
                parcial3=col[13],
                prom_p1=col[14],
                prom_p2=col[15],
                prom_p3=col[16],
                prom_f=col[17],
                faltasp1=col[18],
                faltasp2=col[19],
                faltasp3=col[20],
                cal=col[21],
                prom_cal=col[22],
                calif_final=col[23]
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_datos_academicos_utc.f_espacio_boleta_calif_UTC"
                     " called successfully")

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

    records_list = [report_card.dict() for report_card in records_list]
    return records_list


def report_card_unam_ula(student_enrollment_number: str, period: str) -> list[ReportCardUnam]:
    """
    This function to use banner stored function 'pkg_datos_academicos.f_espacio_boleta_unam_ula'
    """
    logger.debug(f"report_card_unam_ula() accessed")
    logger.debug(f"The incoming data is: "
                 f"student_enrollment_number: {student_enrollment_number}, "
                 f"program: {period}")

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
            "BANINST1.pkg_datos_academicos.f_espacio_boleta_unam_ula",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number, period]
        )

        data = cursor_data.fetchall()

        records_list: list[ReportCardUnam] = []

        for col in data:
            record = ReportCardUnam(
                spriden_id=col[0],
                matricula_unam=col[1],
                alumno=col[2],
                campus=col[3],
                programa=col[4],
                ciclo=col[5],
                bloque=col[6],
                grupo=col[7],
                clave=col[8],
                asignatura=col[9],
                grado=col[10],
                parcial1=col[11],
                parcial2=col[12],
                parcial3=col[13],
                parcial4=col[14],
                prim_vuelta=col[15],
                seg_vuelta=col[16],
                final=col[17],
                conducta1=col[18],
                conducta2=col[19],
                conducta3=col[20],
                conducta4=col[21],
                conducta_final=col[22],
                faltasp1=col[23],
                faltasp2=col[24],
                faltasp3=col[25],
                faltasp4=col[26],
                cal=col[27],
                calif_final=col[28],
                totfal=col[29],
                cp=col[30],
                aut=col[31],
                observaciones=col[32],
                prom_4p=col[33],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_datos_academicos.f_espacio_boleta_unam_ula"
                     " called successfully")

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

    records_list = [report_card_unam.dict() for report_card_unam in records_list]
    return records_list


def academic_history_ula(student_enrollment_number: str, program: str) -> list[AcademicHistory]:
    """
    This function to use banner stored function 'pkg_datos_academicos.f_espacio_historia_academica_ula'
    """
    logger.debug(f"academic_history_ula() accessed")
    logger.debug(f"The incoming data is: "
                 f"student_enrollment_number: {student_enrollment_number}, "
                 f"program: {program}")

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
            "BANINST1.pkg_datos_academicos.f_espacio_historia_academica_ula",
            oracledb.DB_TYPE_CURSOR,
            [student_enrollment_number, program]
        )

        data = cursor_data.fetchall()

        records_list: list[AcademicHistory] = []

        for col in data:

            record = AcademicHistory(
                orden_plan=col[0],
                clave1=col[1],
                clave=col[2],
                materia=col[3],
                calificacion=col[4],
                creditos=col[5],
                area=col[6],
                shrtckn_term_code=col[7],
                periodo=col[8],
                tipo=col[9],
                matricula=col[10],
                alumno=col[11],
                programa=col[12],
                creditos_totales=col[13],
                nivel=col[14],
                smrprle_levl_code=col[15],
                stvlevl_desc=col[16],
                creditos_cubiertos=col[17],
                aprobadas=col[18],
                no_aprobadas=col[19],
                promedio_grado=col[20],
                promedio=col[21],
                rvoe=col[22],
                fecha=col[23],
                dtes=col[24],
                detalles_legales=col[25],
                grado=col[26],
                plantel=col[27],
            )
            records_list.append(record)

        # Commit the changes
        conec.commit()
        # log of confirmation
        logger.debug("Stored function CALL BANINST1.pkg_datos_academicos.f_espacio_historia_academica_ula"
                     " called successfully")

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

    records_list = [academic_history.dict() for academic_history in records_list]
    return records_list
