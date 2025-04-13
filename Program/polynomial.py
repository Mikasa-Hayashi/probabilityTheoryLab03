from math import pow, prod
from combinations import *


def get_and_validate_input_data():
    n = int(input('Введите общее число испытаний n (1 ≤ n ≤ 10): '))
    if not (1 <= n <= 10):
        print('Неверное значение n')
        exit()

    k = int(input('Введите количество исходов k (k ≥ 2): '))
    if k < 2:
        print('Неверное значение k')
        exit()

    m = []
    print('Введите значения m1...mk (целые, сумма должна равняться n):')
    for i in range(k):
        mi = int(input(f'm{i + 1} = '))
        if mi < 0:
            print(f'Неверное значение m{i + 1}')
            exit()
        m.append(mi)

    if sum(m) != n:
        print(f'Ошибка: сумма m1 + ... + mk = {sum(m)} не равна n = {n}')
        exit()

    p = []
    print('Введите значения p1...pk (0 ≤ pi ≤ 1):')
    for i in range(k):
        pi = float(input(f'p{i + 1} = '))
        if not (0 <= pi <= 1):
            print(f'Неверное значение p{i + 1}')
            exit()
        p.append(pi)

    return n, k, m, p


def calc_multinomial_prob(n, k, m, p):
    return fact_with_rep(n, m) * prod([pow(p[i], m[i]) for i in range(k)])


n, k, m, p = get_and_validate_input_data()

print('\nРасчётная формула:')
print('Pn(m₁, m₂, ..., mₖ) = n! / (m₁! * m₂! * ... * mₖ!) * (p₁^m₁ * p₂^m₂ * ... * pₖ^mₖ)')

print(f'\nОтвет: {calc_multinomial_prob(n, k, m, p)}')