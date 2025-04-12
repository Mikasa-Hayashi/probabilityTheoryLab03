from math import pow
from combinations import *


def calculate_bernoulli_prob(n: int, m: int, p: int) -> float:
    q = 1 - p
    combs = comb_without_rep(n, m)
    probability = combs * pow(p, m) * pow(q, n-m)
    return probability


def prob_less_than(n: int, m: int, p: int):
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m))


def prob_more_equal(n: int, m: int, p: int):
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m, n+1))


def prob_between(n: int, m1: int, m2: int, p: int):
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m1, m2+1))