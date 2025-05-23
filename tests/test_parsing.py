from pathlib import Path

from src.utils.parsing import load_athlete_file


def test_load_csv(tmp_path: Path):
    csv = tmp_path / "athletes.csv"
    csv.write_text("player,class,sport,school_name,conference,Summary-2019\nJohn Doe,SR,football,Wake Forest,ACC,True")
    df = load_athlete_file(csv)
    assert not df.empty
    assert bool(df.loc[0, "Summary-2019"]) is True
