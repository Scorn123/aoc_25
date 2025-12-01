from pathlib import Path
from typing import List, Union

INPUT_FOLDER_PATH = Path("../../inputs")


def read_input(day: int, part: int) -> List[str]:
    """
    Read the Advent of Code input for a given day and puzzle part and return a list of lines.

    Parameters:
        day: day number as an int (e.g., 3)
        part: puzzle number as an int (1 or 2)

    Returns:
        A list of lines from the input file (newline characters removed, empty lines preserved).

    Raises:
        TypeError: if day or part are not ints.
        FileNotFoundError: if the input file does not exist.
    """
    if not isinstance(day, int) or not isinstance(part, int):
        raise TypeError("day and part must be integers")

    path = INPUT_FOLDER_PATH / f"day_{day}_{part}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    return path.read_text(encoding="utf-8").splitlines()
