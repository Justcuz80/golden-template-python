from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    default_name: str = "Justin"
