from dataclasses import dataclass
from typing import List

@dataclass
class Athlete:
    player: str
    first_name: str
    last_name: str
    class_year: str
    sport: str
    school_name: str
    conference: str
    years_active: List[int]
