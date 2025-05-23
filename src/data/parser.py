import pandas as pd
from typing import List, Tuple

from src.models.athlete import Athlete


class AthleteDataParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_dataset(self) -> List[Athlete]:
        """Parse consolidated athlete dataset into Athlete objects."""
        df = pd.read_excel(self.file_path)
        athletes: List[Athlete] = []

        for _, row in df.iterrows():
            first_name, last_name = self._parse_name(row.get("player", ""))
            years_active = self._extract_active_years(row)

            athlete = Athlete(
                player=row.get("player", ""),
                first_name=first_name,
                last_name=last_name,
                class_year=row.get("class", ""),
                sport=row.get("sport", ""),
                school_name=row.get("school_name", ""),
                conference=row.get("conference", ""),
                years_active=years_active,
            )
            athletes.append(athlete)

        return athletes

    def _parse_name(self, full_name: str) -> Tuple[str, str]:
        """Parse full name handling special characters like apostrophes."""
        if not isinstance(full_name, str):
            return "", ""
        parts = full_name.strip().split()
        if not parts:
            return "", ""
        first = parts[0]
        last = parts[-1] if len(parts) > 1 else ""
        return first, last

    def _extract_active_years(self, row: pd.Series) -> List[int]:
        """Extract years from Summary-YEAR columns."""
        years: List[int] = []
        for year in range(2016, 2022):
            col = f"Summary-{year}"
            if col in row and pd.notna(row[col]):
                value = str(row[col]).strip().lower()
                if value and value not in {"", "nan", "no", "0"}:
                    years.append(year)
        return years
