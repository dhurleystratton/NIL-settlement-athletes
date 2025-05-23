from __future__ import annotations

import logging
from typing import List, Set

from ..models.profile import SocialProfile

logger = logging.getLogger(__name__)


def deduplicate(profiles: List[SocialProfile]) -> List[SocialProfile]:
    seen: Set[str] = set()
    unique: List[SocialProfile] = []
    for profile in profiles:
        key = f"{profile.platform}:{profile.username.lower()}"
        if key not in seen:
            seen.add(key)
            unique.append(profile)
    logger.info("Deduplicated %d profiles", len(profiles) - len(unique))
    return unique
