import sys
from math import exp, factorial


def get_and_validate_input_data():
    print('Формула Пуассона применяется, если:\n- n > 20\n- p < 0.1\n- λ = n * p ≤ 10\n')

    n = int(input('Введите значение n (n > 0): '))
    if n <= 0:
        print('Ошибка: n должно быть положительным')
        sys.exit()

    p = float(input('Введите значение p (0 < p < 1): '))
    if not (0 < p < 1):
        print('Ошибка: p должно быть в пределах (0, 1)')
        sys.exit()

    interval_mode = input('Хотите рассчитать интервал значений m? (y/n): ').strip().lower() == 'y'

    if interval_mode:
        m1 = int(input('Введите значение m1 (m1 ≥ 0): '))
        m2 = int(input('Введите значение m2 (m2 ≥ m1): '))
        if m1 < 0 or m2 < m1:
            print('Ошибка: некорректные значения m1 и m2')
            sys.exit()
        return n * p, m1, m2
    else:
        m = int(input('Введите значение m (m ≥ 0): '))
        if m < 0:
            print('Ошибка: m должно быть неотрицательным')
            sys.exit()
        return n * p, m, None


def poisson_prob(lam, m):
    return exp(-lam) * (lam ** m) / factorial(m)


# Основной блок
lam, m1, m2 = get_and_validate_input_data()

if m2 is None:
    print('\nФормула:')
    print('P(X = m) = e^(-λ) · λ^m / m!')
    result = poisson_prob(lam, m1)
    print(f'\nОтвет: P(X = {m1}) = {result}')
else:
    print('\nФормула:')
    print('P(m1 ≤ X ≤ m2) = Σ [e^(-λ) · λ^m / m!]')
    result = sum(poisson_prob(lam, m) for m in range(m1, m2 + 1))
    print(f'\nОтвет: P({m1} ≤ X ≤ {m2}) = {result}')