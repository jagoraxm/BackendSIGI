from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int
    host: str
    service_id: str
    service_name: str
    oauth_service_url: str
    access_token_secret: str

    environment: str
    debug: bool
    testing: bool
    secret_key: str

    banner_9_db_user: str
    banner_9_db_password: str
    dsn: str
    dsn_utg: str
    encoding: str

    class Config:
        env_file = ".env"
