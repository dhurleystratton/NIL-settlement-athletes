#!/usr/bin/env python
from __future__ import annotations

import logging
from pathlib import Path

from src.pipeline.processor import process_athletes
from src.utils.parsing import load_athlete_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(path: str) -> None:
    df = load_athlete_file(Path(path))
    profiles = process_athletes(df)
    logger.info("Discovered %d profiles", len(profiles))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <athlete_file>")
    main(sys.argv[1])
