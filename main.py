"""Write one nostalgic childhood-memory sentence to entry.txt."""

import os

ENTRY = "The summer I turned nine, my mother let me stay up past dark to catch fireflies in a jam jar, and I cried when she made me let them go because the light was too beautiful to keep."


def validate_entry(text: str) -> None:
    if not text or len(text) > 200:
        raise SystemExit("entry must be non-empty and at most 200 characters")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
