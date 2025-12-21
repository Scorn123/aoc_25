from pathlib import Path
from typing import  Optional

INPUT_FOLDER_PATH = Path("../inputs")


def read_input(
        day: int,
        *,
        separator: Optional[str] = None,
        split_whitespace: bool = False,
        keep_empty: bool = True,
) -> list[str]:
    """
    Read the Advent of Code input for a given day and return a list of strings.

    Parameters:
        day: day number as an int (e.g., 3)
        separator: string separator to split on (e.g., ",", "|", "\\n\\n").
                   If None and split_whitespace is False, split by lines.
        split_whitespace: if True, split on arbitrary whitespace (like str.split()).
        keep_empty: whether to keep empty strings after splitting.

    Returns:
        A list of strings split according to the chosen method.

    Raises:
        TypeError: if day is not an int.
        FileNotFoundError: if the input file does not exist.
    """
    if not isinstance(day, int):
        raise TypeError("day must be an integer")

    path = INPUT_FOLDER_PATH / f"day_{day}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    text = path.read_text(encoding="utf-8")

    if split_whitespace:
        parts = text.split()
    elif separator is not None:
        parts = text.split(separator)
    else:
        parts = text.splitlines()

    if not keep_empty:
        parts = [p for p in parts if p != ""]

    return parts
