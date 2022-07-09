import pytest

from plain_data import extract_numbers


@pytest.mark.parametrize(
    ("input_data", "expected_response"),
    [
        ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5]),
        ([6, [1, [2, 3], 4], 5], [6, 1, 2, 3, 4, 5]),
        ([[[1, 2,], 3], 4, 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([(1, 2, [3, 4, []]), [5, [6, (7, 8)], 9], 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, ["2", ["tres", 4]], "five"], [1, 2, 4]),
        ([1, [2, [3, {4, 5}]]], [1, 2, 3, 4, 5]),
        ([None, 1], [1])
    ]
)
def test_extract_numbers(input_data, expected_response):
    actual_response: list[int] = extract_numbers(input_data)

    assert actual_response == expected_response
