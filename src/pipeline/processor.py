from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Iterable, List

import pandas as pd

from ..discovery.instagram import InstagramDiscovery
from ..discovery.twitter import TwitterDiscovery
from ..discovery.linkedin import LinkedInDiscovery
from ..models.athlete import Athlete
from ..models.profile import SocialProfile
from .deduplicate import deduplicate
from ..verification.matcher import Matcher

logger = logging.getLogger(__name__)


def process_athletes(df: pd.DataFrame, max_workers: int = 5) -> List[SocialProfile]:
    instagram = InstagramDiscovery()
    twitter = TwitterDiscovery()
    linkedin = LinkedInDiscovery()
    matcher = Matcher()

    athletes = [_row_to_athlete(row) for _, row in df.iterrows()]
    results: List[SocialProfile] = []

    def handle(athlete: Athlete) -> List[SocialProfile]:
        profiles = []
        for discovery in (instagram, twitter, linkedin):
            try:
                profiles.extend(discovery.discover(athlete))
            except Exception as exc:  # pragma: no cover - network errors
                logger.error("Discovery failed for %s: %s", athlete.player, exc)
        scored = matcher.score(athlete, profiles)
        top = [m.profile for m in scored if m.score > 0.5]
        return top

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for profile_list in executor.map(handle, athletes):
            results.extend(profile_list)
    return deduplicate(results)


def _row_to_athlete(row: pd.Series) -> Athlete:
    years = [int(y.replace("Summary-", "")) for y in row.index if y.startswith("Summary-") and row[y]]
    first, last = row["player"].split(maxsplit=1)
    return Athlete(
        player=row["player"],
        first_name=first,
        last_name=last,
        class_year=row["class"],
        sport=row["sport"],
        school_name=row["school_name"],
        conference=row["conference"],
        years_active=years,
    )
