import sys
from math import pow
from combinations import *


def get_and_validate_input_data():
    event_number = int(input('Выберите событие: \n'
                             '1. P_n(k = m)\n'
                             '2. P_n(k < m)\n'
                             '3. P_n(k ≥ m)\n'
                             '4. P_n(m1 ≤ k ≤ m2)\n'
                             '5. Все сразу\n'
                             'Введите соответствующий номер: '))
    if not (1 <= event_number <= 5):
        print('Неверный номер события')
        sys.exit()

    params = {}

    params['p'] = float(input('Введите параметр p (0 ≤ p ≤ 1): '))
    if not (0 <= params['p'] <= 1):
        print('Неверный параметр p')
        sys.exit()

    params['n'] = int(input('Введите параметр n (1 ≤ n ≤ 10): '))
    if not (1 <= params['n'] <= 10):
        print('Неверный параметр n')
        sys.exit()

    if event_number in (1, 3):
        params['m'] = int(input('Введите параметр m (0 ≤ m ≤ n): '))
        if not (0 <= params['m'] <= params['n']):
            print('Неверный параметр m')
            sys.exit()

    elif event_number == 2:
        params['m'] = int(input('Введите параметр m (1 ≤ m ≤ n): '))
        if not (1 <= params['m'] <= params['n']):
            print('Неверный параметр m')
            sys.exit()

    elif event_number == 4:
        params['m1'] = int(input('Введите параметр m1 (0 ≤ m1 < n): '))
        if not (0 <= params['m1'] < params['n']):
            print('Неверный параметр m1')
            sys.exit()

        params['m2'] = int(input('Введите параметр m2 (m1 < m2 ≤ n): '))
        if not (params['m1'] < params['m2'] <= params['n']):
            print('Неверный параметр m2')
            sys.exit()

    else:
        params['m'] = int(input('Введите параметр m (1 ≤ m ≤ n): '))
        if not (1 <= params['m'] <= params['n']):
            print('Неверный параметр m')
            sys.exit()

        params['m1'] = int(input('Введите параметр m1 (0 ≤ m1 < n): '))
        if not (0 <= params['m1'] < params['n']):
            print('Неверный параметр m1')
            sys.exit()

        params['m2'] = int(input('Введите параметр m2 (m1 < m2 ≤ n): '))
        if not (params['m1'] < params['m2'] <= params['n']):
            print('Неверный параметр m2')
            sys.exit()

    return *params.values(), event_number


def calculate_bernoulli_prob(n, k, p):
    q = 1 - p
    combs = comb_without_rep(n, k)
    return combs * pow(p, k) * pow(q, n - k)

def print_formula(n, k, p):
    q = 1 - p
    print('Формула: P_n(k = k) = C(n,k) * p^k * q^(n - k)')

def prob_less_than(n, m, p):
    print('Формула: P_n(k < m) = Σ C(n,k) * p^k * q^(n-k)')
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m))

def prob_more_equal(n, m, p):
    print('Формула: P_n(k ≥ m) = Σ C(n,k) * p^k * q^(n-k)')
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m, n+1))

def prob_between(n, m1, m2, p):
    print('Формула: P_n(m1 ≤ k ≤ m2) = Σ C(n,k) * p^k * q^(n-k)')
    return sum(calculate_bernoulli_prob(n, k, p) for k in range(m1, m2 + 1))



input_data = get_and_validate_input_data()

if input_data[-1] == 1:
    p, n, m, event_number = input_data
    print_formula(n, m, p)
    print(f'Ответ: P_n(k = m) = {calculate_bernoulli_prob(n, m ,p)}\n')

elif input_data[-1] == 2:
    p, n, m, event_number = input_data
    print(f'Ответ: P_n(k < m) = {prob_less_than(n, m, p)}\n')

elif input_data[-1] == 3:
    p, n, m, event_number = input_data
    print(f'Ответ: P_n(k ≥ m) = {prob_more_equal(n, m, p)}\n')

elif input_data[-1] == 4:
    p, n, m1, m2, event_number = input_data
    print(f'Ответ: P_n(m1 ≤ k ≤ m2) = {prob_between(n, m1, m2, p)}\n')

else:
    p, n, m, m1, m2, event_number = input_data
    print_formula(n, m, p)
    print(f'Ответ: P_n(k = m) = {calculate_bernoulli_prob(n, m, p)}\n')
    print(f'Ответ: P_n(k < m) = {prob_less_than(n, m, p)}\n')
    print(f'Ответ: P_n(k ≥ m) = {prob_more_equal(n, m, p)}\n')
    print(f'Ответ: P_n(m1 ≤ k ≤ m2) = {prob_between(n, m1, m2, p)}\n')