# step2/impostors.py

from ..graph.search import GetNeighbours


class GetImpostors():
    def __init__(self, graph):
        pass

    @staticmethod
    def run():
        players = set([str(i) for i in range(10)])
        suspects = set(["1", "4", "5"])
        graph = [
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
        ]
        for i in [1, 4, 5]:
            print(f"Impostors associated with {i}: ", players - GetNeighbours.run(graph, i) - suspects)
