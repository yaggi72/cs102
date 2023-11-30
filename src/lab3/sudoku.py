import pathlib
from random import randint
import typing as tp
from copy import deepcopy
T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    matrix = [values[i:i+n] for i in range(0, len(values), n)]

    return matrix


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера строки, указанной в pos.

    :param grid: Нерешенный судоку.

    :param pos: Позиция элемента для проверки.

    :return: Список уже существующих значений в строке.
    """
    """
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    place_stoka = pos[0]

    return grid[place_stoka]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера столбца, указанного в pos

    :param grid: Нерешенный судоку.

    :param pos: Позиция элемента для проверки

    :return: Список уже существующих элементов в столбце.
    """
    """
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    place_stolb = pos[1]
    stolbik = []

    for stoka in grid:
        stolbik.append(stoka[place_stolb])

    return stolbik


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения из квадрата, в который попадает позиция pos

    :param grid: Нерешенный судоку.

    :param pos: Позиция

    :return: Список существующих значений в блоке.
    """
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    block_nums = []
    # Запишем каординаты.
    place_srtoka = pos[0]
    place_stolbik = pos[1]

    # Левый верхний блок.
    if place_srtoka <= 2 and place_stolbik <= 2:
        for stoka in grid[0:3]:
            for i in range(3):
                block_nums.append(stoka[i])

    # Средний верхний блок.
    elif place_srtoka <= 2 and 3 <= place_stolbik <= 5:
        for stoka in grid[0:3]:
            for i in range(3, 6):
                block_nums.append(stoka[i])

    # Правый верхний блок.
    elif place_srtoka <= 2 and 6 <= place_stolbik <= 8:
        for stoka in grid[0:3]:
            for i in range(6, 9):
                block_nums.append(stoka[i])

    # Левый средний блок.
    elif 3 <= place_srtoka <= 5 and place_stolbik <= 2:
        for stoka in grid[3:6]:
            for i in range(3):
                block_nums.append(stoka[i])

    # Средний средний блок.
    elif 3 <= place_srtoka <= 5 and 3 <= place_stolbik <= 5:
        for stoka in grid[3:6]:
            for i in range(3, 6):
                block_nums.append(stoka[i])

    # Правый средний блок.
    elif 3 <= place_srtoka <= 5 and 6 <= place_stolbik <= 8:
        for stoka in grid[3:6]:
            for i in range(6, 9):
                block_nums.append(stoka[i])

    # Левый нижний блок.
    elif 6 <= place_srtoka <= 8 and place_stolbik <= 2:
        for stoka in grid[6:9]:
            for i in range(3):
                block_nums.append(stoka[i])

    # Средний нижний блок.
    elif 6 <= place_srtoka <= 8 and 3 <= place_stolbik <= 5:
        for stoka in grid[6:9]:
            for i in range(3, 6):
                block_nums.append(stoka[i])

    # Правый нижний блок.
    elif 6 <= place_srtoka <= 8 and 6 <= place_stolbik <= 8:
        for stoka in grid[6:9]:
            for i in range(6, 9):
                block_nums.append(stoka[i])

    return block_nums


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """
    Найти первую свободную позицию в пазле

    :param grid: Нерешенный судоку.

    :return: каорды пустой позиции.
    """
    """
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for stroka in grid:
        for num in stroka:
            if num == '.':

                return grid.index(stroka), stroka.index(num)



def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """
    Вернуть множество возможных значения для указанной позиции!

    :param grid: Нерещенный судоку.

    :param pos: Позиция элемента для поиска значений.

    :return: Множество возможных значений.
    """
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    # Создадим множества из уже существующих значений.
    nums_blok = set(get_block(grid, pos))
    nums_string = set(get_row(grid, pos))
    nums_stolbik = set(get_col(grid, pos))

    # Создаем множкство вариантов для подстановки.
    variants = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # Создадим множество из существующих значений в стобце, строке и блоке.
    set_of_nums_in_srt_block_stolb = nums_stolbik | nums_string | nums_blok

    # Вычтем из возможных вариантов уже существующие и получим ответ.
    possible_nums_block = variants - set_of_nums_in_srt_block_stolb

    return possible_nums_block


gridDictionary = dict()


def dot_count(grid: list[list]) -> int:
    """
    Вернуть кол-во пустых значений в судоку!

    :param grid: Файл с судоку.

    :return: Кол-во пустых значений.
    """
    """
    >>> dot_count([['1','2','.'],['.','.','2'],['1','3','2']])
    3
    >>> dot_count([['1','2','3'],['4','5','6'],['7','8','9']])
    0
    """
    return sum(a.count('.') for a in grid)


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """
    Решение пазла, заданного в grid!

    :param grid: Нерешенное судоку

    :return: Решенный судоку!
    """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    if dot_count(grid) == 0:
        return grid

    pos = find_empty_positions(grid)
    gridDictionary[dot_count(grid)] = [a.copy() for a in grid].copy()
    for x in find_possible_values(grid, find_empty_positions(grid)):
        pos = find_empty_positions(grid)
        dots = dot_count(grid)

        if pos:
            grid[pos[0]][pos[1]] = x
            func = solve(grid)

            if func:
                return func

            if dot_count(grid) == 0:
                return grid

            grid = [a.copy() for a in gridDictionary[dots]].copy()


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """
    Если решение solution верно, то вернуть True, в противном случае False.

    :param solution: Решеный судоку.

    :return: Булево значений, обозначает правильность решения.
    """


    proverka = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for stroka in range(9):
        if set(get_row(solution, (stroka,1))) != proverka:
            return False

    for stolbik in range(9):
        if set(get_col(solution, (1, stolbik))) != proverka:
            return False

    for stoka in range(0, 9, 3):
        for stolbik in range(0, 9, 3):
            if set(get_block(solution, (stoka, stolbik))) != proverka:
                return False

    return True



def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """
    Генерация судоку заполненного на N элементов.

    :param N: Integer сколько должно быть заполненых значений.

    :return: Генерирует судоку с N заполнеными элементами.
    """
    """
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = solve([['.' for _ in range(9)] for _ in range(9)])

    if N > 81:
        return grid
    if N == 0:
        return [['.' for _ in range(9)] for _ in range(9)]
    else:
        while N != -1:
            stroka = randint(0, 8)
            stolbik = randint(0, 8)
            if grid[stroka][stolbik] != '.':
                grid[stroka][stolbik] = '.'
                N -= 1

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)#

#ggogogog
