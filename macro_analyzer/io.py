import csv
from pathlib import Path
from typing import Iterable


class InputError(Exception):
    """User-facing input errors (invalid file, invalid format, etc.)."""


def read_rows(paths: Iterable[str]) -> list[dict[str, str]]:
    """
    Read and combine CSV rows from one or more files.
    Returns a list of dictionaries, where keys are CSV headers.
    """
    rows: list[dict[str, str]] = []
    for p in paths:
        path = Path(p)

        if not path.exists():
            raise InputError(f"File not found: {path}")
        if not path.is_file():
            raise InputError(f"Not a file: {path}")

        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise InputError(f"Empty CSV or missing header row: {path}")

            for row in reader:
                if None in row:
                    raise InputError(f"Malformed CSV row in {path}: {row}")
                rows.append(row)

    return rows
