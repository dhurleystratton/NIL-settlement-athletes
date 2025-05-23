from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Settings:
    apify_token: str

    @classmethod
    def load(cls) -> "Settings":
        token = os.getenv("APIFY_TOKEN")
        if not token:
            logger.warning("APIFY_TOKEN not found in environment")
            token = ""
        return cls(apify_token=token)


settings = Settings.load()
