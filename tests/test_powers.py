from __future__ import annotations

import pytest

from app import calculate_powers


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, {"square": 0, "cube": 0, "fifth_power": 0}),
        (2, {"square": 4, "cube": 8, "fifth_power": 32}),
        (-3, {"square": 9, "cube": -27, "fifth_power": -243}),
    ],
)
def test_calculate_powers(value: int, expected: dict[str, int]) -> None:
    assert calculate_powers(value) == expected


def test_rejects_non_integer_input() -> None:
    with pytest.raises(TypeError):
        calculate_powers("2")  # type: ignore[arg-type]
