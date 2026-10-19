def square(n: int | float) -> int | float:
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a numeric value")
    return n ** 2


def cube(n: int | float) -> int | float:
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a numeric value")
    return n ** 3


def fifth_power(n: int | float) -> int | float:
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a numeric value")
    return n ** 5
