from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    postgres_url: str = "postgresql://postgres:password@postgres:5432/users_db"
    amqp_url: str = "amqp://guest:guest@rabbitmq:5672/"
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'  # Игнорировать лишние переменные
    )

# Создаем настройки с fallback
try:
    settings = Settings()
    print("Settings loaded from .env")
except Exception as e:
    print(f"Warning: Could not load .env: {e}")
    # Используем значения по умолчанию
    settings = Settings(
        postgres_url="postgresql://postgres:password@postgres:5432/users_db",
        amqp_url="amqp://guest:guest@rabbitmq:5672/"
    )