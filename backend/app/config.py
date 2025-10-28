from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
	app_name: str = "StockSmart"
	debug: bool = True
	database_url: str = "sqlite:///./smartshop.db"
	cors_origins: List[str] = ["*"]

	class Config:
		env_file = ".env"


settings = Settings()

