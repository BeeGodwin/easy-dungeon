from maze import Maze
import maze
from play_dungeon import *


from player import Player
from tile import Tile
from tile import Wall
import random
from copy import deepcopy


# TODO refactor tests such that they reflect the updated maze module.


def test_make_rooms():
    assert maze.make_row(5, 1, True) == [False, False, False, False, False]
    assert maze.make_row(3, 2, False) == [True, False, True]
    assert maze.make_row(5, 3, False) == [True, False, True, False, True]
    assert maze.make_row(5, 1, False) == [True, True, True, True, True]
    assert maze.make_row(15, 1, False) == [True for _ in range(15)]


def test_instantiate_tiles():
    m = Maze(size=3)
    bool_maze = [[True, True, True], [False, False, True], [True, True, True]]
    mz = m.instantiate_tiles(bool_maze)
    assert len(mz) == 5
    assert len(mz[0]) == 5
    wall, tile = Wall(), Tile()
    for i in range(len(mz)):
        assert mz[0][i] == wall
        assert mz[i][0] == wall
    assert mz[1][1] == tile
    assert mz[2][1] == wall


def test_move_is_legal():
    random.seed(1)
    mz = Maze(size=5)
    player = Player()
    assert player.x == 1
    assert player.y == 1
    player.next_x = 2
    assert mz.move_is_legal(player)
    player.update_pos()
    player.next_y = 2
    assert not mz.move_is_legal(player)

# def test_room_count():
#     mz = Maze(size=3)
#     assert mz.room_count([[False, False, False],
#                           [False, True, False],
#                           [False, False, False]]) == 1
#     assert mz.room_count([[True, False, True],
#                           [False, True, False],
#                           [True, False, True]]) == 5
#     assert mz.room_count([[False, False, False],
#                           [False, False, False],
#                           [False, False, False]]) == 0
#     assert mz.room_count([[True, True, True],
#                           [True, True, True],
#                           [True, True, True]]) == 1
#
#
# def test_get_adj_tiles():
#     mz = Maze(size=3)
#     maze = [[True for _ in range(3)] for _ in range(3)]
#     assert mz.get_adj_tiles(maze, 1, 1) == [(1, 0), (0, 1), (2, 1), (1, 2)]
#     assert mz.get_adj_tiles(maze, 0, 0) == [(1, 0), (0, 1)]
#     assert mz.get_adj_tiles(maze, 2, 2) == [(2, 1), (1, 2)]
#
#
# def test_flood_fill():
#     mz = Maze(size=3)
#     bools = [[True, True, True], [True, True, True], [True, True, True]]
#     assert mz.flood_fill(bools, 0, 0) == 9
#     assert bools == [[False, False, False], [False, False, False], [False, False, False]]
#     bools = [[True, True, True], [False, False, False], [True, True, True]]
#     assert mz.flood_fill(bools, 0, 0) == 3
#     assert bools == [[False, False, False], [False, False, False], [True, True, True]]
#
#
# def test_make_rooms_in_row():
#     mz = Maze(size=5)
#     assert mz.make_rooms_in_row([True, False, True], 1) == [True, True, True]
#     random.seed(1)  # random.randrange(2) returns 0
#     assert mz.make_rooms_in_row([True, False, True, False, True], 2) == [True, True, True, False, True]
#
#
# def test_join_rooms():
#     mz = Maze(size=5)
#     walls = mz.join_rooms([True, True, True], [False, False, False])
#     random.seed(1)
#     assert walls == [False, False, True]
#
#

#
#
# # def test_complete_maze():  # bit borked!
# #     mz = Maze(size=5)
# #     bools = [[True, True, True], [False, False, True], [True, True, True]]
# #     assert mz.complete_maze(deepcopy(bools)) == bools
# #     bools = [[True, False, True], [True, False, True], [True, False, True]]
# #     bools = mz.complete_maze(bools)
# #     assert mz.room_count(bools) == 1
#
#
# def test_room_coords():
#     mz = Maze(size=5)
#     bools = [[True, True, True], [False, False, True], [True, True, True]]
#     assert sorted(mz.room_coords(bools, 0, 0)) == [
#         (0, 0), (0, 2), (1, 0), (1, 2), (2, 0),(2, 1), (2, 2)]
#
#
