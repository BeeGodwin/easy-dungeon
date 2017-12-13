class MazeTree:
    """Linked list-ish object describing the maze from the player's start point
    as a sequence of coordinate pairs linked by decisions."""

    def __init__(self, mz):
        """Builds a new tree from Maze mz starting at 0, 0."""
        self.root = MazeTreeBranch(mz, None, 0, 0, 'e')  # make an empty tree
        # build the tree in the branch init method, using recursion and
        # by interrogating the maze object.

        # once tree is built, think about useful methods.


class MazeTreeBranch:
    """One branch of a MazeTree. Consists of a parent, an ordered sequence of
    at least one (x, y) tuples, and optionally some children."""

    def __init__(self, mz, parent, x, y, dir):
        self.parent = parent  # prev tile is parent.tiles[-1]
        self.tiles = mz.vector(x, y, dir)
        last_x, last_y = last_tile = self.tiles[-1]
        next_tiles = mz.legal_moves(last_x, last_y)
        if last_tile in next_tiles:
            next_tiles.remove(last_tile)
        for tile in next_tiles:
            pass


