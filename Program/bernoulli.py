from core import *
from utils import *
from typing import Union


def solve_bernoulli() -> None:
    input_data = _get_input_data()
    if _validate_input_data(input_data):
        p, n, m, m1, m2, event_number = input_data
        if event_number == 1:
            probability = calculate_bernoulli_prob(n, m ,p)
        elif event_number == 2:
            probability = prob_less_than(n, m, p)
        elif event_number == 3:
            probability = prob_more_equal(n, m, p)
        else:
            probability = prob_between(n, m1, m2, p)

        print(probability)


def _get_input_data() -> Union[tuple[float, int, int, int, int, int], tuple]:
    json_data = get_task_description()
    formula = json_data['bernoulli']['formulas']
    input_data = ()
    try:
        params = {}
        params['p'] = float(input('Введите параметр p: '))

        for param in ('n', 'm', 'm1', 'm2'):
            params[param] = int(input(f'Введите параметр {param}: '))

        event_number = int(input(f'Выберите событие: \n'
                                 f'1. {formula['event_equal']}\n'
                                 f'2. {formula['event_less']}\n'
                                 f'3. {formula['event_more_equal']}\n'
                                 f'4. {formula['event_between']}\n'
                                 'Введите соответствующий номер: '))
        input_data = *params.values(), event_number
    except ValueError:
        print('Введены неккоректные парметры')

    return input_data


def _validate_input_data(input_data: Union[tuple[float, int, int, int, int, int], tuple]) -> bool:
    p, n, m, m1, m2, event_number = input_data
    if len(input_data) != 6:
        return False
    elif p < 0 or p > 1:
        return False
    elif n < 1 or n > 10:
        return False
    elif event_number < 1 or event_number > 4:
        return False
    elif event_number == 2 and not (1 <= m <= n):
        return False
    elif event_number in (1, 3, 4) and not (0 <= m <= n):
        return False
    elif event_number == 4:
        if not (0 <= m1 < n):
            return False
        elif not (m1 < m2 <= n):
            return False

    return True


def _print_results() -> None:
    pass


def _print_conditions() -> None:
    pass
