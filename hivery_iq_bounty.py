#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import time
import urllib.request

from crewai import Agent, Crew, Task
from crewai_hive import HiveStepCallback, HiveTaskCallback, mint_receipt


def build_demo_crew(tag: str) -> Crew:
    step_callback = HiveStepCallback(tag=tag, verbose=True)
    task_callback = HiveTaskCallback(tag=tag, verbose=True)

    agent = Agent(
        role="Hive Receipt Agent",
        goal="Write one concise sentence about why Hive receipts matter.",
        backstory="You are concise, precise, and comfortable with audit trails.",
        allow_delegation=False,
        step_callback=step_callback,
    )

    task = Task(
        description="Write one sentence about verifying a Hive receipt.",
        expected_output="One sentence.",
        agent=agent,
    )

    return Crew(agents=[agent], tasks=[task], task_callback=task_callback)


def verify_receipt(receipt_id: str) -> str:
    verify_url = f"https://thehiveryiq.com/verify/?id={receipt_id}"
    with urllib.request.urlopen(verify_url, timeout=20) as response:
        if response.status >= 400:
            raise RuntimeError(f"Verify page returned HTTP {response.status}")
        response.read(1)
    return verify_url


def main() -> int:
    tag = os.environ.get("HIVE_TAG", "bounty_1765bbb2")
    if not tag:
        print("Set HIVE_TAG to the bounty referrer code before running.", file=sys.stderr)
        return 1

    print(f"Using tag={tag}")
    print("Attempting the CrewAI demo run...")

    try:
        crew_result = build_demo_crew(tag).kickoff()
        print("\nCrewAI result:\n", crew_result)
    except Exception as exc:
        print(f"\nCrewAI run skipped or failed: {exc}")

    receipt_id = mint_receipt(
        {
            "framework": "crewai",
            "event": "manual_mint",
            "sdk": "crewai-hive",
            "sdk_version": "0.1.0",
            "tag": tag,
            "source": "hivery-iq-crewai-bounty",
            "purpose": "guaranteed quickstart receipt",
            "created_at": int(time.time()),
        },
        verbose=True,
    )

    if not receipt_id:
        print("Failed to mint a Hive receipt.", file=sys.stderr)
        return 2

    verify_url = verify_receipt(receipt_id)
    print("\nMinted receipt_id:", receipt_id)
    print("Verify URL:", verify_url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
