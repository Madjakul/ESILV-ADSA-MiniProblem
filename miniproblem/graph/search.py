# graph/search.py

import queue
from collections import defaultdict


class GetNeighbours():
    def __init__(self, graph):
        self.V = len(graph)
        self.graph = graph

    def get_neigbours(self, node):
        neigbours = []
        [neigbours.append(str(j)) for j in range(self.V) if self.graph[node][j] != 0]
        return set(neigbours)

    @staticmethod
    def run(graph, nodes):
        neighbours = GetNeighbours(graph)
        return neighbours.get_neigbours(nodes)
