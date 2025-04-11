import subprocess
import os

ARTICLE = "Main"

commands = [
    f"latex -synctex=1 {ARTICLE}",
    f"bibtex {ARTICLE}",
    f"latex -synctex=1 {ARTICLE}",
    f"latex -synctex=1 {ARTICLE}",
    f"dvipdfmx {ARTICLE}.dvi"
]

for cmd in commands:
    print(f"🛠 Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Error running: {cmd}, with exit code {result.returncode}")
        break
else:
    print("\n✅ Compilation finished successfully.")
