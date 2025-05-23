# NIL Settlement Athlete Discovery

This project assists in locating and verifying NCAA athlete social media profiles to facilitate outreach for Name, Image, Likeness (NIL) settlement claim acquisition.

## Features
- Discovery modules for Instagram, Twitter/X and LinkedIn powered by Apify actors
- Verification system scoring confidence of profile matches
- Parallel processing for large datasets
- Deduplication across platforms
- Configurable via environment variables

## Project Structure
```
src/
  discovery/
  verification/
  pipeline/
  models/
  config.py
scripts/
data/
  raw/
  processed/
```

## Setup
1. Install dependencies using [Poetry](https://python-poetry.org/).
2. Create a `.env` file with your API keys.
3. Run tests with `pytest`.

