from pathlib import Path

from src.data.parser import AthleteDataParser


def test_parser(tmp_path: Path) -> None:
    csv = tmp_path / "athletes.csv"
    csv.write_text(
        "player,class,sport,school_name,conference,Summary-2019\n"
        "John Doe,SR,football,Wake Forest,ACC,True"
    )
    parser = AthleteDataParser(csv)
    athletes = parser.parse()
    assert len(athletes) == 1
    athlete = athletes[0]
    assert athlete.first_name == "John"
    assert athlete.last_name == "Doe"
    assert athlete.years_active == [2019]
