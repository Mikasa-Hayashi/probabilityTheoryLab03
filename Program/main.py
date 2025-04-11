from bernoulli import *
from polynomial import *
from poisson import *


def _select_task() -> None:
    try:
        task_number = int(input('Выберите номер задачи [1..3]: '))

        if task_number == 1:
            solve_bernoulli()
        elif task_number == 2:
            solve_polynomial()
        elif task_number == 3:
            solve_poisson()
        else:
            raise ValueError
    except ValueError:
        print('Введен некорректный номер задачи')


if __name__ == '__main__':
    _select_task()