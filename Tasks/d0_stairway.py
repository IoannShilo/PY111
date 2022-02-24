from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """


    def lazy_stair_way_path(stair_number: int) -> Union[float, int]:
        """
        Принимает номер ступени, возвращает стоимость до неё
        """
        if stair_number == 0:
            return stairway[stair_number]
        if stair_number == 1:
            return stairway[stair_number]

        current_cost = stairway[stair_number]
        return current_cost + min(lazy_stair_way_path(stair_number-1),
                                  lazy_stair_way_path(stair_number-2))

    return lazy_stair_way_path(len(stairway)-1)



def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    ...
    #stairway - цена ступени
    count_stairs = len(stairway)    # количество ступеней
    total_cost = [0] * count_stairs  # стоимость дойти до ступеней
    # изначальные условия 1 и 2 ступень

    # прямой метод обхода i - стоимость = i - цена + min((i-1) -cost, (i-2) - cost)

    total_cost[0] = stairway[0]  # для первой ступени
    total_cost[1] = stairway[1]  # для второй ступени

    for i in range(2, count_stairs):
        total_cost[i] = stairway[i] + min(total_cost[i - 1], total_cost[i - 2])

    return total_cost[-1]


def reverse_stair_way_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stairs = len(stairway)
    total_cost: list[float] = [float("inf")] * count_stairs

    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])

    for i in range(0, count_stairs):
            total_cost[i + 1] = min(total_cost[i] + stairway[i + 1], total_cost[i + 1])
            total_cost[i + 2] = min(total_cost[i] + stairway[i + 2], total_cost[i + 2])

    total_cost[-1] = min(total_cost[-2] + stairway[-1], total_cost[-1])

    return  total_cost[-1]


