from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


SOURCE_FILENAME = "template Registrazione Live multitraccia.rpp"


def main() -> None:
    script_dir: Path = Path(__file__).resolve().parent
    source_file: Path = script_dir / SOURCE_FILENAME

    if not source_file.is_file():
        raise FileNotFoundError(f"File sorgente non trovato: {source_file}")

    recording_name: str = input("Nome nuova registrazione: ").strip()

    if not recording_name:
        raise ValueError("Il nome della registrazione non può essere vuoto.")

    date_prefix: str = datetime.now().strftime("%Y%m%d")
    folder_name: str = f"{date_prefix} {recording_name}"

    destination_dir: Path = script_dir.parent / folder_name
    destination_dir.mkdir(parents=True, exist_ok=False)

    destination_file: Path = destination_dir / f"{folder_name}{source_file.suffix}"

    shutil.copy2(source_file, destination_file)

    print(f"Creato: {destination_file}")


if __name__ == "__main__":
    main()
