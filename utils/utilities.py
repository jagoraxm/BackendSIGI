from services.logger_service import logger


def log_not_defined_env_var(var_name: str):
    logger.warning(f"{var_name} environment variable is not defined.")
