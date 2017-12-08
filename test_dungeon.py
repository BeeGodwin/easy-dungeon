import maze
from maze import Maze
import play_dungeon
from player import Player
from tile import Tile
from tile import Wall
import random
from copy import deepcopy


def test_make_row():
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


def test_join_rooms():
    random.seed(1)
    walls = maze.join_rooms([True, True, True], [False, False, False])
    assert walls == [True, False, False]


def test_get_adj_tiles():
    mz = [[True for _ in range(3)] for _ in range(3)]
    assert maze.get_adj_tiles(mz, 1, 1) == [(1, 0), (0, 1), (2, 1), (1, 2)]
    assert maze.get_adj_tiles(mz, 0, 0) == [(1, 0), (0, 1)]
    assert maze.get_adj_tiles(mz, 2, 2) == [(2, 1), (1, 2)]


def test_map_room():
    mz = [[True, False, True], [True, False, True], [True, False, True]]
    lst = []
    maze.map_room(mz, lst, 0, 0)
    assert sorted(lst) == [(0, 0), (0, 1), (0, 2)]
    lst = []
    maze.map_room(mz, lst, 2, 0)
    assert sorted(lst) == [(2, 0), (2, 1), (2, 2)]


def test_room_coordinates():
    mz = [[True, False, True], [True, False, True], [True, False, False]]
    room_list = maze.room_coordinates(mz)
    assert room_list == [[(2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2)]]
