import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "The agent said the bug was fixed, so I checked the diff. It had fixed it by deleting the test that caught it."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
