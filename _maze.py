from tile import *
import random
from copy import copy, deepcopy
from math import sqrt


# TODO- whole thing needs a refactor?
# TODO- what is a function, what is a method?
# seems like most of the maze creation, and anything that deals with a partial maze, is a function.

class Maze:
    """the game board. Essentially a 2D array of tiles."""

    # TODO- sort out which methods are class methods, and which are object methods.

    def __init__(self, size=17, tile_px=32):
        self.size = size  # tiles square. Should be odd.
        self.tile_px = tile_px
        self.maze = self.make_maze()

    def make_rooms_in_row(self, lst, n):  # make func
        """Given a list of tiles (a row), remove just enough wall tiles to have
        it contain n rooms."""
        count = self.room_count([copy(lst)])
        can_remove = [i for i in range(len(lst)) if not lst[i]]
        while count > n:
            remove_wall = random.randrange(0, len(can_remove))
            lst[can_remove[remove_wall]] = True
            count = self.room_count([copy(lst)])
        return lst

    def join_rooms(self, row_n, wall_row):  # make func.
        """Given row_n and a wall_row, modify wall_row."""
        # for each room in row_n, flip a random bool in wall_row within its range.
        wrk = [copy(row_n)]
        for i in range(len(wrk[0])):
            rm_sz = self.flood_fill(wrk, i, 0)
            if rm_sz == 1:
                wall_row[i] = True
            elif rm_sz == 0:
                continue
            else:
                idx = random.randrange(i, rm_sz + i, step=2)
                wall_row[idx] = True
        return wall_row

    def init_maze(self):  # could make func, but could just refactor so we make the right thing in the first place.
        """returns a square 2d array of booleans, size  self.size -2.
        Values are initialised with True for a path, False for a wall."""
        sz = self.size - 2
        paths = [True if i % 2 == 0 else False for i in range(sz)]
        walls = [False for _ in range(sz)]
        maze = [copy(paths) if i % 2 == 0 else copy(walls) for i in range(sz)]
        return maze

    def room_count(self, bools):  # is there a way to not have to copy before sending to this? also, func.
        """Counts rooms. Takes a 2d array of bools. Copy the array before
        sending (bad coding there!)"""
        n = 0

        for y in range(len(bools)):
            for x in range(len(bools[0])):
                if bools[y][x]:
                    n += 1
                    self.flood_fill(bools, x, y)
        return n


#

    def flood_fill(self, bools, x, y, n=0):  # func!
        """for the cell with value True at x, y in 2D array bools, first
         mark it False, and if adjacent cells are True, call flood_fill
         on them also. Fills any area bounded by False values."""
        if bools[y][x]:
            bools[y][x] = False
            n += 1
            for (x_2, y_2) in self.get_adj_tiles(bools, x, y):
                if bools[y_2][x_2]:
                    n = self.flood_fill(bools, x_2, y_2, n)
            return n
        else:
            return n

    @staticmethod
    def get_adj_tiles(ary, x, y):  # func
        """returns a list of (x, y) tuples describing adjacent coordinates in
        array ary. Respects the edge of the board and corners."""
        y_size = len(ary) - 1
        x_size = len(ary[0]) - 1
        lst = []
        if y > 0:
            lst.append((x, y - 1))
        if x > 0:
            lst.append((x - 1, y))
        if x < x_size:
            lst.append((x + 1, y))
        if y < y_size:
            lst.append((x, y + 1))
        return lst

    def bools_to_mz(self, bools):  # Given that this array is gonna be our obj, this ought to be a method.
        """Takes the 'inner' maze represented by 2d array bools, and turns it into
        a maze of tiles. Returns this maze."""
        wall_top = [Wall(px=self.tile_px) for _ in range(len(bools[0]) + 2)]
        wall_bottom = deepcopy(wall_top)
        maze = [wall_top]

        for y in range(len(bools)):

            row = [Wall(px=self.tile_px)]
            for x in range(len(bools[0])):
                if bools[y][x]:
                    row.append(Tile(px=self.tile_px))
                else:
                    row.append(Wall(px=self.tile_px))
            row.append(Wall(px=self.tile_px))

            maze.append(row)
        maze.append(wall_bottom)

        return maze

    def complete_maze(self, bools):  # see if you still need to do this when at bottom of rabbit hole
        """Takes an almost-finished maze of boolean values. Ensures that the
        maze consists of one 'room', and if not, modifies it so it does.
        Returns completed maze of boolean values."""
        # # TODO- solve the issue of orphaned rooms. still borked
        # print(self.room_count(deepcopy(bools)))
        # # plan B!
        # while self.room_count(deepcopy(bools)) > 1:
        #     count = self.room_count([copy(bools[-1])])
        #     # bools[-1] = self.make_rooms_in_row(bools[-1], 1)

        return bools

    def room_coords(self, bools, x, y):  # func again, given that it's used in construction.
        """returns a coordinate list of all the tiles in the room containing
        tile at (x, y)."""
        coord_lst = [(x, y)]

        def recurse(x, y):
            for (adj_x, adj_y) in self.get_adj_tiles(bools, x, y):
                if (adj_x, adj_y) not in coord_lst and bools[adj_y][adj_x]:
                    coord_lst.append((adj_x, adj_y))
                    recurse(adj_x, adj_y)

        recurse(x, y)

        return coord_lst

    def move_is_legal(self, player):  # definitely a method.
        """Check to see that the player's next move is legal and return True / False."""
        if type(self.maze[player.next_y][player.next_x]) == Tile:  # might we want an attr on the tile?
            return True
        return False


