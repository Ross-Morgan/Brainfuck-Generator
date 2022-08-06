import math


def closest_square(n: int) -> int:
    root = math.sqrt(n)

    adjacent_squares = [
        math.floor(root) ** 2,
        math.ceil(root) ** 2,
    ]

    square_diffs = [s - root for s in adjacent_squares]

    return adjacent_squares[square_diffs.index(min(square_diffs))]


def smallest_sum_factor_pair(n: int) -> tuple[int, int]:
    pairs = [(i, int(n / i)) for i in range(1, int(n ** 0.5)+1) if n % i == 0]
    pair_sums = list(map(sum, pairs))

    return pairs[pair_sums.index(min(pair_sums))]


def nice_factor_pair(n: int) -> tuple[tuple[int, int], int]:
    if n % 1:
        raise ValueError("n must be an integer")

    while True:
        pass
