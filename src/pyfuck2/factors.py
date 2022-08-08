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
    original = n

    if (n < 0) or (n % 1):
        raise ValueError("n must be a positive integer")

    pairs = [(i, int(n / i)) for i in range(1, int(math.sqrt(n))+1) if n % i == 0]
    pair_sums = list(map(sum, pairs))

    pair = pairs[pair_sums.index(min(pair_sums))]
    pair = int(math.copysign(pair[0], original)), pair[1]

    return pair


def smallest_sum_factors_and_remainder(n: int) -> tuple[tuple[int, int], int]:
    """
    Calculate 2 factors and additional number with smallest sum that result
    in any given integer 'n'


    """
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

    factors.append(sum(smallest_sum_factor_pair(original)))
    origins.append((original, 0))

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


print(smallest_sum_factors_and_remainder(49))
