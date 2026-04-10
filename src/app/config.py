import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    default_name: str
    log_level: str
    app_env: str

    @classmethod
    def from_env(cls) -> "Settings":
        """Build settings from environment variables."""
        return cls(
            default_name=os.getenv("APP_DEFAULT_NAME", "Justin"),
            log_level=os.getenv("APP_LOG_LEVEL", "INFO").upper(),
            app_env=os.getenv("APP_ENV", "development"),
        )
