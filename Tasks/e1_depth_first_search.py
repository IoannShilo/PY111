from typing import Hashable, List
import networkx as nx


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#
#     path_node = []
#     visited_nodes = {node: False for node in g.nodes}
#     wait_nodes = [] # stack
#     wait_nodes.append(start_node)
#     visited_nodes[start_node] = True
#
#     while wait_nodes:
#         current_node = wait_nodes.pop()
#         path_node.append(current_node)
#         neighbours = g[current_node]
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)
#                 visited_nodes[neighbour] = True


    # return path_node


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    visited_nodes = {node: False for node in g.nodes}
    node_path = []

    def recursion_dfs(current_node):
        if visited_nodes[current_node]:
            return None
        visited_nodes[current_node] = True
        node_path.append(current_node)

        neighbours = g[current_node]
        for neighbour in neighbours:
            recursion_dfs(neighbour)

        return node_path

    return recursion_dfs(start_node)