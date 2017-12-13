# class MazeTree:
#     """Linked list-ish object describing the maze from the player's start point
#     as a sequence of coordinate pairs linked by decisions."""
#
#     def __init__(self, mz):
#         """Builds a new tree from Maze mz starting at 0, 0."""
#         self.tiles = set()
#         self.root = MazeTreeBranch(mz, self, None, 1, 1, 'e')  # make an empty tree
#         # build the tree in the branch init method, using recursion and
#         # by interrogating the maze object.
#
#         # once tree is built, think about useful methods.
#
#
# class MazeTreeBranch:
#     """One branch of a MazeTree. Consists of a parent, an ordered sequence of
#     at least one (x, y) tuples, and optionally some children."""
#
#     def __init__(self, mz, tree, parent, x, y, dr):
#         self.parent = parent
#         self.dr = dr
#         self.x = x
#         self.y = y
#         self.tiles = mz.vector(x, y, dr)  # rdoesn't seem to be returning right vals.
#
#         for tile in self.tiles:
#             tree.tiles.add(tile)
#
#         self.chn = {}
#
#         last_x, last_y = last_tile = self.tiles[-1]
#         next_tiles = mz.legal_moves(last_x, last_y)
#
#         if last_tile in next_tiles:
#             next_tiles.remove(last_tile)
#
#         for tile in next_tiles:
#             if tile not in tree.tiles:
#                 dr = dir_helper(last_tile, tile)
#                 new_x, new_y = tile
#                 self.chn[dr] = MazeTreeBranch(mz, tree, self, new_x, new_y, dr)
#
#     def __str__(self):
#         s = 'Branch at ({}, {}) going {} for {} tiles. {} children.'.format(
#             self.x, self.y,
#             self.dr, len(self.tiles), len(self.chn)
#         )
#         return s
#
#
# def dir_helper(loc1, loc2):
#     """Takes two (x, y) tuples representing adjacent tiles, and
#     returns a single character from {'n', 'e', 'w', 's'} representing
#     the direction of loc1 to loc2."""
#     x1, y1 = loc1
#     x2, y2 = loc2
#     if x1 == x2:
#         if y2 > y1:
#             return 's'
#         else:
#             return 'n'
#     if x2 > x1:
#         return 'e'
#     else:
#         return 'w'
