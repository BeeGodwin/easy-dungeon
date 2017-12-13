from math import sqrt
import random
from copy import copy, deepcopy
from tile import *


class Maze:
    """the game board. Essentially a 2D array of tiles."""

    def __init__(self, size=17, tile_px=32):
        self.size = size  # tiles square. Should be odd.
        self.tile_px = tile_px
        self.lgc_mz = make_maze(self.size)
        self.mz = self.instantiate_tiles()

    def instantiate_tiles(self):
        """Takes the 'inner' maze represented by 2d array bools, and turns it into
        a maze of tiles. Returns this maze."""
        wall_top = [Wall(px=self.tile_px) for _ in range(len(self.lgc_mz[0]) + 2)]
        wall_bottom = deepcopy(wall_top)
        maze = [wall_top]

        for y in range(len(self.lgc_mz)):
            row = [Wall(px=self.tile_px)]

            for x in range(len(self.lgc_mz[0])):
                if self.lgc_mz[y][x]:
                    row.append(Tile(px=self.tile_px))
                else:
                    row.append(Wall(px=self.tile_px))
            row.append(Wall(px=self.tile_px))

            maze.append(row)

        maze.append(wall_bottom)

        return maze

    def move_is_legal(self, loc):
        """Check to see that the player's next move is legal and return True / False."""
        x, y = loc
        if type(self.mz[y][x]) == Tile:  # might we want an attr on the tile?
            return True
        return False

    def legal_moves(self, x, y):
        """Returns a list of (x, y) tuples representing legal moves from this
        (x, y)."""
        moves = ((a_x, a_y) for (a_x, a_y) in get_adj_tiles(self.mz, x, y))
        return list(filter(lambda loc: self.move_is_legal(loc), moves))


def make_maze(size):
    """returns a maze ready for play."""
    mz = []
    r = int(sqrt(size))  # rooms per row

    for i in range(size):  # make rows
        if i % 2 == 0:
            mz.append(make_row(size, r, False))
        else:
            mz.append(join_rooms(mz[i - 1], make_row(size, r, True)))

    finalise(mz)
    mz = repair(mz)

    return mz


def finalise(mz):
    """Given a nearly-done maze, hacks the fuck out of it to bodge our way
    to the finish line. Modifies mz."""
    rooms = room_coordinates(mz)

    if len(rooms) == 1:
        return

    bubble = rooms.pop(0)

    if len(bubble) == 1:
        x, y = bubble[0]
        pop_bubble(mz, x, y)
    else:
        max_y = len(mz) - 1
        cands = []
        for i in range(len(bubble)):
            x, y = bubble.pop(0)
            if y == max_y and x % 2 == 0:
                cands.append((x, y))
        x, y = random.choice(cands)
        pop_bubble(mz, x, y)

    finalise(mz)


def repair(mz):
    """Takes a boolean maze that has had the fuck hacked out of it by the
    previous algo, and fixes it. Looks at the last 3 rows and fills in walls
    the penultimate (wall) row that don't affect the room count."""
    last_rows = deepcopy(mz[-3:])
    # rm_count = len(room_coordinates(last_rows))
    for i in range(len(last_rows[1])):
        if last_rows[1][i]:
            last_rows[1][i] = False
            rm_count = len(room_coordinates(mz[:-3] + last_rows))
            if rm_count > 1:
                last_rows[1][i] = True

    return mz[:-3] + last_rows


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


def get_adj_tiles(ary, x, y):
    """returns a list of (x, y) tuples describing adjacent coordinates in
    array ary. Respects the edge of the board and corners. Doesn't care about
    what's in the tile."""
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


def room_coordinates(boolean_maze):
    """returns a coordinate list of all the tiles in the room containing
    tile at (x, y). Sorted by size, with small rooms first."""
    wrk = deepcopy(boolean_maze)
    room_list = []

    for y in range(len(wrk)):
        for x in range(len(wrk)):
            if wrk[y][x]:
                room = []
                map_room(wrk, room, x, y)
                room_list.append(room)

    room_list.sort(key=len)

    return room_list


def map_room(mz_cpy, coord_lst, x, y):
    """Recurse thru 2d boolean array mz_cpy and list all (x, y) coordinate pairs.
    Modify both the array and the coord list."""
    coord_lst.append((x, y))
    mz_cpy[y][x] = False
    for (adj_x, adj_y) in get_adj_tiles(mz_cpy, x, y):
        if mz_cpy[adj_y][adj_x] and (adj_x, adj_y) not in coord_lst:
            map_room(mz_cpy, coord_lst, adj_x, adj_y)


def pop_bubble(bn_mz, x, y):
    """Given an (x, y) in bn_mz, flip one of its adjacent False values to True.
    Modifies bn_mz and returns the (x, y) that was flipped, or None."""
    adj = get_adj_tiles(bn_mz, x, y)
    for i in range(len(adj)):
        a_x, a_y = adj.pop(0)
        if not bn_mz[a_y][a_x]:
            adj.append((a_x, a_y))
    if len(adj) > 0:
        flip = random.randrange(0, len(adj))
        flip_x, flip_y = adj[flip][0], adj[flip][1]
        bn_mz[flip_y][flip_x] = True


def vector_helper(dir, x, y):
    """Takes a single char dir from {'n', 'e', 'w', 's'} and an x, y, and gives you the next tile
    in that direction."""
    if dir == 'n' or dir == 's':
        adj_x = x
        if dir == 'n':
            adj_y = y - 1
        else:
            adj_y = y + 1
    else:
        adj_y = y
        if dir == 'e':
            adj_x = x + 1
        else:
            adj_x = x - 1
    return (adj_x, adj_y)


def dir_helper(loc1, loc2):
    """Takes two (x, y) tuples representing adjacent tiles, and
    returns a single character from {'n', 'e', 'w', 's'} representing
    the direction of loc1 to loc2."""
    x1, y1 = loc1
    x2, y2 = loc2
    if x1 == x2:
        if y2 > y1:
            return 's'
        else:
            return 'n'
    if x2 > x1:
        return 'e'
    else:
        return 'w'
