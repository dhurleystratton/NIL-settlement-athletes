from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, HttpUrl


class Platform(str, Enum):
    instagram = "instagram"
    twitter = "twitter"
    linkedin = "linkedin"


class SocialProfile(BaseModel):
    platform: Platform
    username: str
    profile_url: HttpUrl
    confidence: float
