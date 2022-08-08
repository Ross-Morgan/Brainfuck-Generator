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
    n = abs(n)
    pairs = [(i, int(n / i)) for i in range(1, int(n ** 0.5)+1) if n % i == 0]
    pair_sums = list(map(sum, pairs))

    return pairs[pair_sums.index(min(pair_sums))]


def smallest_sum_factors_and_remainder(n: int) -> tuple[tuple[int, int], int]:
    original = n
    n = abs(n)

    if n % 1:
        raise ValueError("n must be an integer")

    factors: list[int] = []
    origins: list[tuple[int, int]] = []

    # Number of iterations to check
    runs = 5

    # Multiples to check for factors
    k = 4
    a = -k

    # Round down to nearest multiple of k
    n -= n % k
    a += n % k

    n += k

    for _ in range(runs):
        if n < k:
            break

        n -= k
        a += k
        factors.append(sum(smallest_sum_factor_pair(n)) + (original - n))
        origins.append((n, (original - n)))

    if not factors:
        return (0, 0), original
    return smallest_sum_factor_pair(origins[factors.index(min(factors))][0]), origins[factors.index(min(factors))][1]
