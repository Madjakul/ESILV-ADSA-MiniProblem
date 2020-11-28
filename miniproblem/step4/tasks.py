# step4/tasks.py

from collections import defaultdict
from ..graph.backtracking import Graph


class Tasks():
    def __init__(self):
        pass

    @staticmethod
    def run():
        graph = defaultdict(list)
        crewmatesMap = [
            [0, 5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 5, 4, 4, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 0, 4, 0, 5, 0, 8, 0, 0, 0, 0, 0, 0],
            [3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 3, 0, 0, 3, 3, 1, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 4, 3, 0, 2, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 2, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 4, 6, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 7, 6, 8, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0]
        ]
        for i in range(14):
            for j in range(14):
                    if crewmatesMap[i][j] != 0:
                        graph[i + 1].append(j + 1)
        response = Graph()
        print(response.hamilton(dict(graph), 14, 5))