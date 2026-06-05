from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7

    mail_username: str = ""
    mail_password: str = ""
    mail_from: str = ""
    mail_server: str = ""
    mail_port: int = 587


    notification_hour: int = 8

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()