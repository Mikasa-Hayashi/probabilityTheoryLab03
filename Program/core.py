from math import pow
from combinations import *


def calculate_bernoulli_prob(n: int, m: int, p: int) -> float:
    q = 1 - p
    combs = comb_without_rep(n, m)
    probability = combs * pow(p, m) * pow(q, n-m)
    return probability
