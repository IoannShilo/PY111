from typing import Hashable, List
from collections import deque
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    path_nodes = []  # сюда должны помещаться узлы из очереди / "сгоревшие узлы" результат
    visited_nodes = {node: False for node in g.nodes} # словарь из непосещенных узлов
    # конец справа, начало слева
    wait_nodes = deque()  # очередь из узлов которые ожидают обхода
    wait_nodes.append(start_node)  # подожгли первый узел

    while wait_nodes:
        current_node = wait_nodes.popleft()  # достаем горящий узел, чтобы поджечь соседей, которые еще не горят
        path_nodes.append(current_node) # формируем путь обхода
        visited_nodes[current_node] = True # делаем узел сгоревшим

        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour) # подожгли соседа
                visited_nodes[neighbour] = True

    return path_nodes



