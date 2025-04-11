from core import *
from typing import Union


def solve_bernoulli() -> None:
    data = _get_input_data()

    if len(data) == 5:
        # probability =
        pass

def _get_input_data() -> Union[tuple[int, int, int, int, int], tuple]:
    input_data = ()
    try:
        param_p = int(input('Введите параметр p: '))
        param_n = int(input('Введите параметр n: '))
        param_m = int(input('Введите параметр m: '))
        param_m1 = int(input('Введите параметр m1: '))
        param_m2 = int(input('Введите параметр m2: '))
        input_data = param_p, param_n, param_m, param_m1, param_m2
    except ValueError:
        print('Введены неккоректные парметры')

    return input_data


def _print_results() -> None:
    pass


def _print_conditions() -> None:
    pass
