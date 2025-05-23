from __future__ import annotations

from pathlib import Path
from typing import List

from ..models.athlete import Athlete
from ..utils.parsing import load_athlete_file


class AthleteDataParser:
    """Parse raw athlete files into `Athlete` objects."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)

    def parse(self) -> List[Athlete]:
        df = load_athlete_file(self.path)
        athletes: List[Athlete] = []
        for _, row in df.iterrows():
            years = [
                int(col.replace("Summary-", ""))
                for col in df.columns
                if col.startswith("Summary-") and bool(row[col])
            ]
            first, last = row["player"].split(maxsplit=1)
            athletes.append(
                Athlete(
                    player=row["player"],
                    first_name=first,
                    last_name=last,
                    class_year=row["class"],
                    sport=row["sport"],
                    school_name=row["school_name"],
                    conference=row["conference"],
                    years_active=years,
                )
            )
        return athletes
