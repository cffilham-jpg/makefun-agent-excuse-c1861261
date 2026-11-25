"""Write the chosen excuse about shipping a bug at 3 AM.
The line lands with one twist: even the agent's tests were asleep.
Tests provide the specific concrete noun that keeps the joke immediate.
"""

import hashlib
import os
import tempfile
from pathlib import Path

LINE = "I shipped the bug at 3 AM, when even my tests were asleep."
CHAR_LIMIT = 200


def _resolve_output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        path = Path(env_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
    try:
        out = Path("out")
        out.mkdir(parents=True, exist_ok=True)
        return out
    except OSError:
        return Path(tempfile.mkdtemp(prefix="makefun-agent-excuse-c1861261-"))


def validate(path: Path) -> None:
    data = path.read_bytes()
    text = data.decode("utf-8")
    assert text == LINE, "entry.txt content does not match LINE"
    assert 1 <= len(text) <= CHAR_LIMIT, "line must be 1-200 chars"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert not text.endswith("\n"), "no trailing newline"
    assert text == text.strip(), "no leading/trailing whitespace"


def main() -> None:
    out_dir = _resolve_output_dir()
    entry = out_dir / "entry.txt"
    entry.write_bytes(LINE.encode("utf-8"))
    validate(entry)
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
