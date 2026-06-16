import os
import subprocess
import sys


def commit_step(message):
    if not message:
        raise ValueError("Commit message is required.")

    try:
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"Committed changes with message: '{message}'")
    except subprocess.CalledProcessError as exc:
        print(f"Git command failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/commit_step.py \"Commit message\"")
        sys.exit(1)
    commit_step(sys.argv[1])
