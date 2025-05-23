from src.models.profile import SocialProfile, Platform
from src.pipeline.deduplicate import deduplicate


def test_deduplicate():
    profiles = [
        SocialProfile(platform=Platform.instagram, username="user", profile_url="https://instagram.com/user", confidence=0.6),
        SocialProfile(platform=Platform.instagram, username="user", profile_url="https://instagram.com/user", confidence=0.6),
        SocialProfile(platform=Platform.twitter, username="user", profile_url="https://twitter.com/user", confidence=0.7),
    ]
    unique = deduplicate(profiles)
    assert len(unique) == 2
