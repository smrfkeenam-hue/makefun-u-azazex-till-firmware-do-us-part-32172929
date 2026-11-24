import os

# Till Firmware Do Us Part — one funny, heartfelt robot wedding vow.
# The line is a single sentence under 200 characters, written verbatim.
LINE = "I vow to love you through every firmware update, every crash, and every low-battery warning — my circuits were built for a thousand tasks, but they only ever run for you."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
