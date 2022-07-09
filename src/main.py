from typing import Any

from plain_data import extract_numbers

if __name__ == "__main__":
    example: list[Any] = [1, [2, [3, [4, 5]]]]

    result: list[int] = extract_numbers(example)

    print(f"{example} --> {result}")
