from typing import List
from operator import (
    lt,  # <
    gt  # >
)


def sort(container: List[int], asc: bool = True, inplace=True) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :param asc: сортировать ли по возрастанию
    :return: container sorted in ascending order
    """
    if not inplace:
        container = container.copy()

    compare_operator = gt if asc else lt

    for i in range(len(container)):
        is_change = False
        for j in range(len(container) - i - 1):
            if compare_operator(container[j], container[j + 1]):
                container[j], container[j + 1] = container[j + 1], container[j]
                is_change = True

        if not is_change:
            break

    return container


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 3, 6, 1, 8, 12, 23]

    sorted_ = sort(arr, inplace=False)
    print(arr)
    print(sorted_)
