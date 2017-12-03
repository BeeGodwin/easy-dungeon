from maze import Maze
from player import Player
from tile import Tile
from tile import Wall
from play_dungeon import *


def test_make_maze():
    mz = Maze(size=15)
    assert len(mz.maze) == 15
    assert len(mz.maze[0]) == 15
    for tile in mz.maze[0]:
        assert type(tile) == Wall
    for tile in mz.maze[14]:
        assert type(tile) == Wall
    for i in range(len(mz.maze)):
        assert type(mz.maze[i][0]) == Wall
        assert type(mz.maze[i][14]) == Wall


def test_room_count():
    mz = Maze(size=3)
    assert mz.room_count() == 1
    mz = Maze(size=5)
    assert mz.room_count() == 4
    mz = Maze(size=7)
    assert mz.room_count() == 9
    mz = Maze(size=5)
    mz.maze[1][2] = Tile()
    assert mz.room_count() == 3


def test_get_adj_tiles():
    mz = Maze(size=3)
    assert mz.get_adj_tiles(1, 1) == [(0, 1), (0, 2), (1, 2), (2, 1)]
    assert mz.get_adj_tiles(0, 0) == [(1, 0), (0, 1)]


def test_flood_fill():
    mz = Maze(size=3)
    bools = [[True, True, True], [True, True, True], [True, True, True]]
    mz.flood_fill(bools, 1, 1)
    assert bools == [[False, False, False], [False, False, False], [False, False, False], ]
    bools = [[True, True, True], [False, False, False], [True, True, True]]
    mz.flood_fill(bools, 0, 0)
    assert bools == [[False, False, False], [False, False, False], [True, True, True]]
