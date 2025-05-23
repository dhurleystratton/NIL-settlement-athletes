from __future__ import annotations

from typing import List
from pydantic import BaseModel


class Athlete(BaseModel):
    player: str
    first_name: str
    last_name: str
    class_year: str
    sport: str
    school_name: str
    conference: str
    years_active: List[int]
