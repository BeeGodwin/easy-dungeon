from tile import *
import random


class Maze:
    """the game board. Essentially a 2D array of tiles."""

    def __init__(self, size=17, tile_px=32):
        self.size = size  # tiles square. Should be odd.
        self.tile_px = tile_px
        # self.maze = self.make_maze()

    def make_maze(self):
        """returns a maze ready for play. PH code here!"""
        init_maze = self.init_maze()  # inner maze of bools
        # feed row 0 to make_rooms_in_row and copy it
            # copy in row 1 (walls)
            # feed row 2 to make_rooms_in_row and copy it
            # join rooms by removing walls in row 1
        # when adding the final row, resolve to 1 room
        # turn boolean array into objects, adding outer walls
        maze = self.bools_to_mz(init_maze)
        return maze

    def make_rooms_in_row(self, lst, n):
        """Given a 2d array containing a list of one list of tiles (a row),
        remove just enough wall tiles to have it contain n rooms."""
        # TODO refactor so it expects a list of bools.
        # TODO could this be iterative, and do all the rows at once?
        tile_px = lst[0][0].px
        count = self.room_count(lst)
        can_remove = [i for i in range(len(lst[0])) if type(lst[0][i]) == Wall]
        can_remove.pop(-1)
        can_remove.pop(0)
        while count > n:
            remove = random.randrange(0, len(can_remove) - 1)
            lst[0][remove] = Tile(px=tile_px)
        return lst

    def join_rooms(self, mz, n):
        """Given a 2d maze of bools with the most recent row at the bottom,
        remove wall tiles from the most recent solid row until we are back to
        n rooms."""
        pass

    def init_maze(self):
        """returns a square 2d array of booleans, size  self.size -2.
        Values are initialised with True for a path, False for a wall."""
        sz = self.size - 2
        paths = [True if i % 2 == 0 else False for i in range(sz)]
        walls = [False for _ in range(sz)]
        maze = [paths if i % 2 == 0 else walls for i in range(sz)]
        return maze

    def room_count(self, bools):
        """Counts rooms. Takes a 2d array of bools."""
        n = 0
        for y in range(len(bools)):
            for x in range(len(bools[0])):
                if bools[y][x]:
                    n += 1
                    self.flood_fill(bools, x, y)
        return n

    def flood_fill(self, bools, x, y):
        """for the cell with value True at x, y in 2D array bools, first
         mark it False, and if adjacent cells are True, call flood_fill
         on them also. We've effectively filled a 'room'."""
        bools[y][x] = False
        for (x_2, y_2) in self.get_adj_tiles(x, y):
            if bools[y_2][x_2]:
                self.flood_fill(bools, x_2, y_2)

    def get_adj_tiles(self, x, y):
        """returns a list of (x, y) tuples describing adjacent coordinates.
        Respects the edge of the board and corners."""
        size = self.size - 1
        lst = []
        if y > 0:
            lst.append((x, y - 1))
        if x > 0:
            lst.append((x - 1, y))
        if x < size:
            lst.append((x + 1, y))
        if y < size:
            lst.append((x, y + 1))
        return lst

    def mz_to_bools(self):
        """returns an image of the maze as a 2d array of bools, where True means
        a tile is passable, and False means a wall."""
        bools = []
        return bools

    def bools_to_mz(self, bools):
        """Takes the 'inner' maze represented by 2d array bools, and turns it into
        a maze of tiles. Returns this maze."""
        maze = []
        return maze

    #     t_px, size = self.tile_px, self.size
    #     mz = [[Wall(px=t_px) for _ in range(size)] for _ in range(size)]
    #     cell_row = False
    #     cell_open = False
    #     for row in mz:
    #         if cell_row:
    #             for i in range(len(row)):
    #                 if cell_open:
    #                     row[i] = Tile(px=t_px)
    #                 cell_open = not cell_open
    #         cell_row = not cell_row
    #         cell_open = False
    #     return mz
