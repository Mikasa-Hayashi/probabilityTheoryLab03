from task_01_solver import *
from task_02_solver import *


def _select_task() -> None:
    try:
        task_number = int(input('Выберите номер задачи [1..2]: '))

        if task_number == 1:
            solve_task_01()
        elif task_number == 2:
            solve_task_02()
        else:
            raise ValueError
    except ValueError:
        print('Введен некорректный номер задачи')


if __name__ == '__main__':
    _select_task()