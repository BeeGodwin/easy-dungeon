from maze import Maze
from player import Player
from tile import Tile
from tile import Wall
from play_dungeon import *


def test_init_maze():
    mz = Maze(size=15)
    assert len(mz.init_maze()) == 15
    assert len(mz.init_maze()[0]) == 15
    for tile in mz.init_maze()[0]:
        assert type(tile) == Wall
    for tile in mz.init_maze()[14]:
        assert type(tile) == Wall
    for i in range(len(mz.init_maze())):
        assert type(mz.init_maze()[i][0]) == Wall
        assert type(mz.init_maze()[i][14]) == Wall


def test_room_count():  # works! but will break once I'm actually making mazes.
    mz = Maze(size=3)
    assert mz.room_count(mz.maze) == 1
    mz = Maze(size=5)
    assert mz.room_count(mz.maze) == 4
    mz = Maze(size=7)
    assert mz.room_count(mz.maze) == 9
    mz = Maze(size=5)
    mz.maze[1][2] = Tile()
    assert mz.room_count(mz.maze) == 3
    mz.maze[2][1] = Tile()
    assert mz.room_count(mz.maze) == 2
    mz = Maze(size=17)
    assert mz.room_count(mz.maze) == 64


def test_get_adj_tiles():
    mz = Maze(size=3)
    assert mz.get_adj_tiles(1, 1) == [(1, 0), (0, 1), (2, 1), (1, 2)]
    assert mz.get_adj_tiles(0, 0) == [(1, 0), (0, 1)]
    assert mz.get_adj_tiles(2, 2) == [(2, 1), (1, 2)]


def test_flood_fill():
    mz = Maze(size=3)
    bools = [[True, True, True], [True, True, True], [True, True, True]]
    mz.flood_fill(bools, 1, 1)
    assert bools == [[False, False, False], [False, False, False], [False, False, False], ]
    bools = [[True, True, True], [False, False, False], [True, True, True]]
    mz.flood_fill(bools, 0, 0)
    assert bools == [[False, False, False], [False, False, False], [True, True, True]]


def test_make_rooms_in_row():
    pass


def test_join_rooms():
    pass