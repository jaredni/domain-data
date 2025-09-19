import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    WHOIS_API_URL: str = os.getenv("WHOS_API_URL", "https://www.whoisxmlapi.com/whoisserver")
    WHOIS_API_KEY: str = os.getenv("WHOIS_API_KEY", "")


settings = Settings()

