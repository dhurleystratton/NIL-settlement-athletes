from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def load_athlete_file(path: Path) -> pd.DataFrame:
    logger.info("Loading athlete file %s", path)
    if path.suffix in {'.xlsx', '.xls'}:
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)
    summary_cols = [c for c in df.columns if c.startswith('Summary-')]
    for col in summary_cols:
        df[col] = df[col].fillna(False).astype(bool)
    return df
