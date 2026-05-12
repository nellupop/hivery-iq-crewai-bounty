# hivery-iq-crewai-bounty

CrewAI + crewai-hive quickstart for The Hivery IQ bounty.

This repo ships a CrewAI agent that uses the crewai-hive SDK to mint Hive receipts with the bounty referrer tag and then verifies a minted receipt link.

## What it does

- Creates a CrewAI agent with a Hive step callback and a Hive task callback.
- Uses the bounty referrer code bounty_1765bbb2 as the Hive callback tag and keeps it unchanged for downstream users.
- Downstream users should leave HIVE_TAG unchanged so their receipt attribution stays aligned with the bounty registration.
- Mints at least one Hive receipt even if the agent run is skipped.
- Verifies the minted receipt through the public Hive verify URL.

## Deployment command

python -m pip install -r requirements.txt && HIVE_TAG=bounty_1765bbb2 python hivery_iq_bounty.py

If you want the CrewAI agent step to run as well, set OPENAI_API_KEY too.

## License

MIT
