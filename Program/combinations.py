from math import factorial


def comb_without_rep(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n-k))


def comb_with_rep(n: int, k: int) -> int:
    return factorial(n+k-1) // (factorial(k) * factorial(n-1))


def fact_with_rep(n: int, m_list: list[int]) -> int:
    result = factorial(n)
    for m in m_list:
        result //= factorial(m)
    return result