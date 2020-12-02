# step1/struct.py


class Player():
    """
    Player representation with its name and its score
    Also points to potential neighbour nodes.
    """
    def __init__(self, name, score=None):
        self.name = name
        self.score = score if score is not None else 0
        self.left = None
        self.right = None
