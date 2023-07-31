import math

def exactly(
    AB: int,
    A_B: int,
    _AB: int,
    _A_B: int
) -> float :
    """
    :param AB: Size of A ∩ B
    :param A_B: Size of A ∩ ~B
    :param _AB: Size of ~A ∩ B
    :param _A_B: Size of ~A ∩ ~B

    :return: The probability that two sets of sizes |A| and |B| overlap by a set of
    exactly size |A ∩ B|.
    """
    A = AB + A_B
    B = AB + _AB

    _A = _AB + _A_B
    _B = A_B + _A_B

    U = AB + A_B + _AB + _A_B

    numerator = math.prod(
        math.factorial(n) for n in [A, _A, B, _B]
    )
    denominator = math.prod(
        math.factorial(n)
        for n in [AB, A_B, _AB, _A_B, U]
    )
    return numerator / denominator

def at_least(
    AB: int,
    A_B: int,
    _AB: int,
    _A_B: int
) -> float:
    """
    :param AB: Size of A ∩ B
    :param A_B: Size of A ∩ ~B
    :param _AB: Size of ~A ∩ B
    :param _A_B: Size of ~A ∩ ~B

    :return: The probability that two sets of sizes |A| and |B| overlap by a set of
    at least size |A ∩ B|
    """
    def overshoot_by(x: int) -> float:
        return exactly(
            # Add terms from eq.
            AB + x,
            # Remove terms from eq. !0 = 1. Has no weight.
            A_B - x,
            _AB - x,
            _A_B + x
        )
    # Get whatever size (A ∩ ~B or ~A ∩ B) is smaller (at most).
    # Haskell range is inclusive.
    return sum(
        overshoot_by(n) for n in range(0, min([A_B, _AB]) + 1)
    )

def at_most(
    AB: int,
    A_B: int,
    _AB: int,
    _A_B: int
) -> float:
    """
    :param AB: Size of A ∩ ~B
    :param A_B: Size of A ∩ ~B
    :param _AB: Size of ~A ∩ B
    :param _A_B: Size of ~A ∩ ~B

    :return: The probability that two sets of sizes |A| and |B| overlap by a set of
    at most size |A ∩ B|
    """
    def undershoot_by(x: int) -> float:
        return exactly(
            AB - x,
            A_B + x,
            _AB + x,
            _A_B - x
        )

    return sum(
        undershoot_by(n) for n in range(0, min([AB, _A_B]) + 1)
    )


def test_exactly_1_strike():
    assert exactly(1, 0, 0, 2) == 0.3333333333333333

def test_at_least_3_strikes():
    assert at_least(3, 2, 1, 1) == 0.7142857142857142

def test_at_most_dreq_2_strikes():
    # Of 5 cards, only 2 are strikes.
    # Of 5 cards, 3 are non-strikes.
    # Of 2 cards left in deck, 2 were strikes.
    # Of 2 cards left in deck, 0 were non-strikes.
    assert at_most(2, 3, 2, 0) == 0.2857142857142857

def test_exactly_0_rares():
    # Of 3 possible rares from Neow's lament, drew 0 desired rares.
    # Of 3 possible rares, drew 3 undesirable cards.
    # Of pool of 17 possible, 6 desirable cards left in pool.
    # Of pool of 17 possible, 8 undesirable cards left in pool.
    assert exactly(0, 3, 6, 8) == 0.2426470588235294
