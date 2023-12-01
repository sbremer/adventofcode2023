import typing as ty
from pathlib import Path

folder_inputs = Path(__file__).parent.parent / "inputs"


def get_lines(day: int) -> ty.List[str]:
    file = folder_inputs / f"{day}.txt"
    return file.read_text().splitlines()
