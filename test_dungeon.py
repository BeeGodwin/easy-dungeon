from maze import Maze
from player import Player
from tile import Tile
from tile import Wall
from play_dungeon import *


def test_init_maze():
    mz = Maze(size=3)
    assert mz.init_maze()[0][0]


def test_room_count():
    mz = Maze(size=3)
    assert mz.room_count([[False, False, False],
                          [False, True, False],
                          [False, False, False]]) == 1
    assert mz.room_count([[True, False, True],
                          [False, True, False],
                          [True, False, True]]) == 5
    assert mz.room_count([[False, False, False],
                          [False, False, False],
                          [False, False, False]]) == 0
    assert mz.room_count([[True, True, True],
                          [True, True, True],
                          [True, True, True]]) == 1


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