import os
from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    app_name: str = "Luca"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
