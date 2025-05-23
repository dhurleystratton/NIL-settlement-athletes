from __future__ import annotations

import logging
from typing import List

import pandas as pd
from pydantic import BaseModel

from ..models.athlete import Athlete
from ..models.profile import SocialProfile

logger = logging.getLogger(__name__)


class ProfileMatch(BaseModel):
    profile: SocialProfile
    score: float


class Matcher:
    """Basic confidence scorer using simple heuristics."""

    def score(self, athlete: Athlete, profiles: List[SocialProfile]) -> List[ProfileMatch]:
        matches: List[ProfileMatch] = []
        athlete_name = athlete.player.lower()
        for profile in profiles:
            score = 0.0
            if athlete.first_name.lower() in profile.username.lower():
                score += 0.3
            if athlete.last_name.lower() in profile.username.lower():
                score += 0.3
            if athlete.school_name.lower().replace(" ", "") in profile.username.lower():
                score += 0.2
            matches.append(ProfileMatch(profile=profile, score=min(score, 1.0)))
        return matches
