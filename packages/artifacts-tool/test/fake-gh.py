import json
import os
from sys import argv

# Log all invocations by appending to gh.log
with open("gh.log", "at") as f:
    print(
        json.dumps(argv, indent=None, separators=(",", ":")),
        file=f
    )

# Simulate `gh release view` behavior based on FAKE_GH_RELEASE_EXISTS env var
if len(argv) >= 3 and argv[1] == "release" and argv[2] == "view":
    if os.environ.get("FAKE_GH_RELEASE_EXISTS", "0") == "1":
        exit(0)
    else:
        exit(1)
