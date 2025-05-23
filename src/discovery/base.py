from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Iterable, List

from apify_client import ApifyClient
from tenacity import retry, stop_after_attempt, wait_fixed

from ..config import settings
from ..models.athlete import Athlete
from ..models.profile import SocialProfile

logger = logging.getLogger(__name__)


class BaseDiscovery(ABC):
    platform: str

    def __init__(self) -> None:
        self.client = ApifyClient(settings.apify_token)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    @abstractmethod
    def discover(self, athlete: Athlete) -> List[SocialProfile]:
        pass


__all__ = ["BaseDiscovery"]
