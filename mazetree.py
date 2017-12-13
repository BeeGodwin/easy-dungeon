class MazeTree:
    """Linked list-ish object describing the maze from the player's start point
    as a sequence of coordinate pairs linked by decisions."""

    def __init__(self, mz):
        """Builds a new tree from Maze mz starting at 0, 0."""
        self.root = MazeTreeBranch(mz, None, 0, 0)  # make an empty tree
        # build the tree in the branch init method, using recursion and
        # by interrogating the maze object.

        # once tree is built, think about useful methods.


class MazeTreeBranch:
    """One branch of a MazeTree. Consists of a parent, an ordered sequence of at least one
    (x, y) tuples, and a pair of children."""

    def __init__(self, mz, parent, x, y):

        self.parent = parent

        self.x = x
        self.y = y

        # self.direction = self.set_direction(mz)

        self.tiles = 0

        self.child_n = None
        self.child_e = None
        self.child_w = None
        self.child_s = None

    def set_direction(self, mz):
        pass


