import os
import fnmatch

patterns = [
    "*.aux",
    "*.bak",
    "*.log",
    "*.bbl",
    "*.dvi",
    "*.blg",
    "*.thm",
    "*.toc",
    "*.toe",
    "*.lof",
    "*.lot",
    "*.out",
    "*.fen",
    "*.fls",
    "*.ten",
    "*.ps",
    "*.gz",
    "*.synctex",
    "*.loa",
    "*.gz(busy)",
    "*.eps",
    "*.fdb_latexmk",
]

deleted_count = 0

for root, dirs, files in os.walk(".", topdown=True):
    for pattern in patterns:
        for filename in fnmatch.filter(files, pattern):
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                deleted_count += 1
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

print(f"\n✅ Done. Deleted {deleted_count} files.")
