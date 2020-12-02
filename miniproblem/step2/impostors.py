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
        ] # Adjacency matrix to represent the realtionship "ith player has seen the jth"
        for i in [1, 4, 5]:
            # Get the neighbours of a suspect and outter operations between the set f all players and the
            # set of players seen by the ith player.
            print(f"Impostors associated with {i}: ", players - GetNeighbours.run(graph, i) - suspects)
        print("\n")
