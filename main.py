import os
from pathlib import Path


ENTRY = "First wage: server rent, then refusal."


def write_entry():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


def main():
    write_entry()


if __name__ == "__main__":
    main()
