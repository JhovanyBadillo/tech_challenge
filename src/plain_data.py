from typing import Any
from collections import abc

def extract_numbers(data: list[Any]) -> list[int]:
    numbers: list[int] = []

    for elem in data:
        if isinstance(elem, abc.Iterable) and not isinstance(elem, str):
            # when elem is a string and since a string is an iterable, it ends
            # in an infinite loop of recursive calls. So we exclude str.
            numbers.extend(extract_numbers(elem))
        else:
            # elem is a single value, maybe an integer... or not
            try:
                number: int = int(elem)
                numbers.append(number)
            except (ValueError, TypeError):
                pass
    
    return numbers
        