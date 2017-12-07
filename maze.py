from math import sqrt
import random
from copy import copy, deepcopy
from tile import *


class Maze:
    """the game board. Essentially a 2D array of tiles."""

    def __init__(self, size=17, tile_px=32):
        self.size = size  # tiles square. Should be odd.
        self.tile_px = tile_px
        self.mz = self.instantiate_tiles(make_maze(self.size))

    def instantiate_tiles(self, bool_mz):  # Given that this array is gonna be our obj, this ought to be a method.
        """Takes the 'inner' maze represented by 2d array bools, and turns it into
        a maze of tiles. Returns this maze."""
        wall_top = [Wall(px=self.tile_px) for _ in range(len(bool_mz[0]) + 2)]
        wall_bottom = deepcopy(wall_top)
        maze = [wall_top]

        for y in range(len(bool_mz)):
            row = [Wall(px=self.tile_px)]

            for x in range(len(bool_mz[0])):
                if bool_mz[y][x]:
                    row.append(Tile(px=self.tile_px))
                else:
                    row.append(Wall(px=self.tile_px))
            row.append(Wall(px=self.tile_px))

            maze.append(row)

        maze.append(wall_bottom)

        return maze

    def move_is_legal(self, player):  # definitely a method.
        """Check to see that the player's next move is legal and return True / False."""
        if type(self.mz[player.next_y][player.next_x]) == Tile:  # might we want an attr on the tile?
            return True
        return False


def make_maze(size):
    """returns a maze ready for play."""
    mz = []
    r = int(sqrt(size))  # rooms per row

    for i in range(size):  # make rows
        if i % 2 == 0:
            mz.append(make_row(size, r, False))
        else:
            mz.append(join_rooms(mz[i - 1], make_row(size, r, True)))

    # mz[-2] = join_rooms(mz[-1], mz[-2])  # has to be a better solution!

    return mz


def make_row(size, r, wall):
    """returns a list of boolean values. True means a tile, False means a wall.
    one row of our maze."""
    if wall:
        return [False for _ in range(size)]

    row = [True if i % 2 == 0 else False for i in range(size)]
    rmv_lst = [i for i in range(1, size, 2)]
    num_to_rmv = (size // 2 + 1) - r
    for i in range(num_to_rmv):
        j = random.randrange(0, len(rmv_lst))
        rmv = rmv_lst.pop(j)
        row[rmv] = True

    return row


def join_rooms(row_n, wall_row):
    """Given row_n and a wall_row, modify wall_row."""
    # for each room in row_n, flip a random bool in wall_row within its range.
    rooms = []
    current_room = []
    for i in range(len(row_n)):
        if row_n[i]:
            current_room.append(i)
        else:
            rooms.append(copy(current_room))
            current_room = []
    if len(current_room) > 0:
        rooms.append(current_room)

    for room in rooms:
        if len(room) > 1:
            i = random.randrange(room[0], room[-1], 2)
            wall_row[i] = True
        else:
            wall_row[room[0]] = True
    return wall_row


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


def list_room_coordinates(boolean_maze):
    """returns a coordinate list of all the tiles in the room containing
    tile at (x, y)."""
    # TODO modify this function so that it returns a list of lists.
    coord_lst = [(x, y)]

    def recurse(x, y):
        for (adj_x, adj_y) in get_adj_tiles(boolean_maze, x, y):
            if (adj_x, adj_y) not in coord_lst and boolean_maze[adj_y][adj_x]:
                coord_lst.append((adj_x, adj_y))
                recurse(adj_x, adj_y)

    recurse(x, y)
    return coord_lst

# def room_count(bools):  # is there a way to not have to copy before sending to this? also, func.
#     """Counts rooms. Takes a 2d array of bools. Copy the array before
#     sending (bad coding there!)"""
#     n = 0
#
#     for y in range(len(bools)):
#         for x in range(len(bools[0])):
#             if bools[y][x]:
#                 n += 1
#                 self.flood_fill(bools, x, y)
#     return n
#
#
# def flood_fill(bools, x, y, n=0):  # func!
#     """for the cell with value True at x, y in 2D array bools, first
#      mark it False, and if adjacent cells are True, call flood_fill
#      on them also. Fills any area bounded by False values."""
#     if bools[y][x]:
#         bools[y][x] = False
#         n += 1
#         for (x_2, y_2) in self.get_adj_tiles(bools, x, y):
#             if bools[y_2][x_2]:
#                 n = self.flood_fill(bools, x_2, y_2, n)
#         return n
#     else:
#         return n
#

#
#
# # def complete_maze(self, bools):  # see if you still need to do this when at bottom of rabbit hole
# #     """Takes an almost-finished maze of boolean values. Ensures that the
# #     maze consists of one 'room', and if not, modifies it so it does.
# #     Returns completed maze of boolean values."""
# #     # print(self.room_count(deepcopy(bools)))
# #     # # plan B!
# #     # while self.room_count(deepcopy(bools)) > 1:
# #     #     count = self.room_count([copy(bools[-1])])
# #     #     # bools[-1] = self.make_rooms_in_row(bools[-1], 1)
# #
# #     return bools
#

#
