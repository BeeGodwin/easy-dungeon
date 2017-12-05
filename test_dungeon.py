from maze import Maze
from player import Player
from tile import Tile
from tile import Wall
from play_dungeon import *
import random


def test_init_maze():
    mz = Maze(size=9)
    maze = mz.init_maze()
    assert len(maze) == 7
    assert len(maze[0]) == 7
    assert maze[0] == [True, False, True, False, True, False, True]
    assert maze[1] == [False, False, False, False, False, False, False]
    for i in range(5):
        assert maze[i] == maze[i + 2]


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
    maze = [[True for _ in range(3)] for _ in range(3)]
    assert mz.get_adj_tiles(maze, 1, 1) == [(1, 0), (0, 1), (2, 1), (1, 2)]
    assert mz.get_adj_tiles(maze, 0, 0) == [(1, 0), (0, 1)]
    assert mz.get_adj_tiles(maze, 2, 2) == [(2, 1), (1, 2)]


def test_flood_fill():
    mz = Maze(size=3)
    bools = [[True, True, True], [True, True, True], [True, True, True]]
    assert mz.flood_fill(bools, 0, 0) == 9
    assert bools == [[False, False, False], [False, False, False], [False, False, False]]
    bools = [[True, True, True], [False, False, False], [True, True, True]]
    assert mz.flood_fill(bools, 0, 0) == 3
    assert bools == [[False, False, False], [False, False, False], [True, True, True]]


def test_make_rooms_in_row():
    mz = Maze(size=5)
    assert mz.make_rooms_in_row([True, False, True], 1) == [True, True, True]
    random.seed(1)  # random.randrange(2) returns 0
    assert mz.make_rooms_in_row([True, False, True, False, True], 2) == [True, True, True, False, True]


def test_join_rooms():
    mz = Maze(size=5)
    walls = mz.join_rooms([True, True, True], [False, False, False])
    random.seed(1)
    assert walls == [False, False, True]


def test_bools_to_maze():
    mz = Maze(size=5)
    bools = [[True, True, True], [False, False, True], [True, True, True]]
    maze = mz.bools_to_mz(bools)
    assert len(maze) == 5
    assert len(maze[0]) == 5
    wall, tile = Wall(), Tile()
    for i in range(len(maze)):
        assert maze[0][i] == wall
        assert maze[i][0] == wall
    assert maze[1][1] == tile
    assert maze[2][1] == wall


# def test_complete_maze():
#     pass


def test_room_coords():
    mz = Maze(size=5)
    bools = [[True, True, True], [False, False, True], [True, True, True]]
    assert mz.room_coords(bools, 0, 0) == [
        (0, 0), (1, 0), (2, 0), (1, 2), (0, 2), (1, 2), (2, 2)]