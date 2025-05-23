import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data.parser import AthleteDataParser


def test_parse_name_simple():
    parser = AthleteDataParser('dummy.xlsx')
    assert parser._parse_name("A'Lique Terry") == ("A'Lique", "Terry")
    assert parser._parse_name("De'Andre Johnson") == ("De'Andre", "Johnson")
    assert parser._parse_name("Mary Jane Smith") == ("Mary", "Smith")
    assert parser._parse_name("John O'Connor") == ("John", "O'Connor")


def test_extract_active_years(tmp_path):
    data = {
        'player': ['Test Player'],
        'Summary-2016': [float('nan')],
        'Summary-2017': ['yes'],
        'Summary-2018': ['7 Att, 24 Yds'],
        'Summary-2019': [''],
        'Summary-2020': [None],
        'Summary-2021': ['no'],
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / 'athletes.xlsx'
    df.to_excel(file_path, index=False)

    parser = AthleteDataParser(str(file_path))
    athletes = parser.parse_dataset()
    assert len(athletes) == 1
    athlete = athletes[0]
    assert athlete.years_active == [2017, 2018]
    assert athlete.first_name == 'Test'
    assert athlete.last_name == 'Player'