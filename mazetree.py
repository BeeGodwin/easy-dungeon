class MazeTree:
    """Linked list-ish object describing the maze from the player's start point
    as a sequence of coordinate pairs linked by decisions."""

    def __init__(self, mz, x, y):
        """Builds a new tree from origin x, y. mz is a 2d boolean array. x, y
        describes a cell with value True."""
        # this is like a linked list.
        self.root = None  # make an empty tree
        self.maze_walk(mz, x, y)
        # need to iterate or recurse thru the maze
        # & make branches
        # build a dict of (x, y) keys mapped to MazeTreeBranch vals.

    def maze_walk(self, mz, x, y):
        """Build the initial tree."""
        self.root = MazeTreeBranch(self, x, y)
        pass


class MazeTreeBranch:
    """One branch of a MazeTree. Consists of a parent, an ordered sequence of at least one
    (x, y) tuples, and a pair of children."""

    def __init__(self, parent, x, y):

        self.parent = parent

        self.x = x
        self.y = y

        self.direction = self.set_direction(mz)

        self.tiles = 0

        self.child_n = None
        self.child_e = None
        self.child_w = None
        self.child_s = None

    def set_direction(self, mz):
        pass


