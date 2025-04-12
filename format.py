import subprocess
from pathlib import Path

extensions = [".tex", ".bib", ".bst"]
base_dir = Path(".")  # 当前目录

for file in base_dir.rglob("*"):
    if file.suffix in extensions:
        print(f"🧹 Formatting {file}")
        result = subprocess.run(["latexindent", "-w", "-l", str(file)], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            print(f"❌ Failed to format {file}")
