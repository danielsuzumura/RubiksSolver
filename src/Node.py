class Node():
    """
        Node class used in A*
    """
    def __init__(self, parent=None, cube=None, move=None):
        self.parent = parent
        self.cube = cube
        self.previousMove = move
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.cube == other.cube
    
    def __lt__(self, other):
        return self.f < other.f