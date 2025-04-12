import shutil
import subprocess
import os
from pathlib import Path

ARTICLE = "Main"
FIGURE_DIR = Path("./figures")
SUPPORTED_EXTS = [".png", ".jpg", ".jpeg"]

if shutil.which("magick") is None:
    print("❌ ImageMagick 未安装或未加入 PATH，请先安装并配置好后重试。")
    exit(1)

def convert_to_eps():
    print("🔄 Converting images to .eps...")
    for ext in SUPPORTED_EXTS:
        for img_path in FIGURE_DIR.glob(f"*{ext}"):
            eps_path = img_path.with_suffix(".eps")
            if not eps_path.exists():
                print(f"🖼  Converting {img_path.name} → {eps_path.name}")
                result = subprocess.run(["magick", str(img_path), str(eps_path)])
                if result.returncode != 0:
                    print(f"❌ Failed to convert {img_path} to EPS")

def compile_latex():
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
        #    break
    else:
        print("\n✅ Compilation finished successfully.")

if __name__ == "__main__":
    convert_to_eps()
    compile_latex()

