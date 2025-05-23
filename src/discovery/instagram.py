from __future__ import annotations

import logging
from typing import List

from apify_client import ActorCaller

from .base import BaseDiscovery
from ..models.athlete import Athlete
from ..models.profile import Platform, SocialProfile

logger = logging.getLogger(__name__)


class InstagramDiscovery(BaseDiscovery):
    platform = Platform.instagram

    def __init__(self) -> None:
        super().__init__()
        self.actor = self.client.actor("apify/instagram-profile-scraper")

    def discover(self, athlete: Athlete) -> List[SocialProfile]:
        logger.info("Discovering Instagram for %s", athlete.player)
        run = self.actor.call(run_input={"search": athlete.player})
        items = run["items"] if run else []
        profiles = []
        for item in items:
            profiles.append(
                SocialProfile(
                    platform=self.platform,
                    username=item.get("username", ""),
                    profile_url=item.get("url", ""),
                    confidence=0.0,
                )
            )
        return profiles
