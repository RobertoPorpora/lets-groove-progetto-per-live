#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
import os


SCRIPT_DIR = Path(__file__).resolve().parent

RPP_FILES = [
    SCRIPT_DIR / "Let's Groove Live.rpp",
    SCRIPT_DIR / "Royalty free music.rpp",
]

def open_with_default_app(path: Path):
    if not path.exists():
        raise FileNotFoundError(path)

    if sys.platform.startswith("win"):
        os.startfile(str(path))

    elif sys.platform == "darwin":
        subprocess.Popen(
            ["open", str(path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )

    else:
        subprocess.Popen(
            ["xdg-open", str(path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )


def run_setup_script(recording_name: str) -> Path:
    setup = SCRIPT_DIR / "live-recording-setup.py"

    result = subprocess.run(
        [
            sys.executable,
            str(setup),
            recording_name,
        ],
        cwd=SCRIPT_DIR,
        text=True,
        capture_output=True,
        check=True,
    )

    for line in result.stdout.splitlines():
        if line.startswith("CREATED_RPP="):
            return Path(line.removeprefix("CREATED_RPP="))

    raise RuntimeError(
        "Il setup non ha restituito il percorso del file creato.\n"
        f"Output:\n{result.stdout}"
    )


def main():
    if len(sys.argv) < 2:
        raise SystemExit(
            "Uso: python launcher.py <nome registrazione>"
        )

    recording_name = sys.argv[1]

    new_rpp = run_setup_script(recording_name)

    open_with_default_app(new_rpp)

    for rpp in RPP_FILES:
        open_with_default_app(rpp)


if __name__ == "__main__":
    main()
