from collections import Counter
from typing import List

from tasks.tasks2.exception import InvalidFileName


def get_file_name(name: str, all_names: List[str]) -> str:
    if not is_valid_name(name):
        raise InvalidFileName(
            f"Invalid filename {name}. Filename must not contains duplicate characters")
    max_len: int = len(max(all_names, key=len))
    diff_len = max_len - len(name)
    if diff_len:
        name = f"{name}{'_' * diff_len}"
    if diff_len < 0:
        raise InvalidFileName(
            f"Invalid filename {name}. "
            f"The length of the filename must be less or equal to the length of the filenames in the list")
    return name


def is_valid_name(name: str) -> bool:
    count = Counter(name)
    return len(count) == len(name)
