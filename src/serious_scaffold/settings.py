"""Settings Module."""
import logging
from logging import getLevelName
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Project settings."""

    logging_level: Optional[str] = getLevelName(logging.INFO)
    """Default logging level for the project."""

    class Config:
        """Config for project settings."""

        env_prefix = "SERIOUS_SCAFFOLD_"


class GlobalSettings(BaseSettings):
    """System level settings."""

    ci: bool = False


settings = Settings()
"""Singleton instance for project specific settings."""

global_settings = GlobalSettings()
"""Singleton instance for system level settings."""
