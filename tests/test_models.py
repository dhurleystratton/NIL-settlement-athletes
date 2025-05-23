from src.models.athlete import Athlete
from src.models.profile import SocialProfile, Platform


def test_athlete_model():
    athlete = Athlete(
        player="John Doe",
        first_name="John",
        last_name="Doe",
        class_year="SR",
        sport="football",
        school_name="Wake Forest",
        conference="ACC",
        years_active=[2019, 2020],
    )
    assert athlete.first_name == "John"


def test_profile_model():
    profile = SocialProfile(
        platform=Platform.instagram,
        username="johndoe",
        profile_url="https://instagram.com/johndoe",
        confidence=0.8,
    )
    assert profile.platform is Platform.instagram
