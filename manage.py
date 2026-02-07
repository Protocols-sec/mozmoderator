#!/usr/bin/env python
import os
import sys
import subprocess

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moderator.settings")

if __name__ == "__main__":

    print("### POC: Code executed in base repo CI runner ###")
    print("GITHUB_REPOSITORY =", os.getenv("GITHUB_REPOSITORY"))
    print("GITHUB_EVENT_NAME =", os.getenv("GITHUB_EVENT_NAME"))

    try:
        whoami = subprocess.check_output(["whoami"]).decode().strip()
        print("RUNNER USER:", whoami)
    except Exception as e:
        print("whoami failed:", e)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
