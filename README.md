# hivery-iq-crewai-bounty

CrewAI + crewai-hive quickstart for The Hivery IQ bounty.

This repo ships a CrewAI agent that uses the crewai-hive SDK to mint Hive receipts with the bounty referrer tag and then verifies a minted receipt link.

## What it does

- Creates a CrewAI agent with a Hive step callback and a Hive task callback.
- Passes the bounty referrer code through the callback tag using HIVE_TAG.
- Mints at least one Hive receipt even if the agent run is skipped.
- Verifies the minted receipt through the public Hive verify URL.

## One-command run

Run: python -m pip install -r requirements.txt && HIVE_TAG=YOUR_REFERRER_CODE python hivery_iq_bounty.py

If you want the CrewAI agent step to run as well, set OPENAI_API_KEY too.

## License

MIT
