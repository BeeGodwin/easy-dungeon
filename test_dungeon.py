import maze
from maze import Maze
import play_dungeon
from player import Player
from fog import FogLayer
from tile import Tile
from tile import Wall
import random
from copy import deepcopy
from pygame import Rect, Color


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
    assert mz == [[True, False, True], [True, False, True], [True, False, False]]


def test_pop_bubble():
    mz = [[True, False, True], [False, False, True], [True, True, True]]
    maze.pop_bubble(mz, 0, 0)
    assert len(maze.room_coordinates(mz)) == 1


def test_finalise():
    mz = [[True, False, True], [False, False, True], [True, True, True]]
    maze.finalise(mz)
    assert len(maze.room_coordinates(mz)) == 1
    mz = [[False, True, False, False, False],
          [False, True, True, True, True],
          [True, True, False, True, False],
          [True, False, False, False, False],
          [True, False, True, True, True]]
    maze.finalise(mz)
    assert len(maze.room_coordinates(mz)) == 1
    assert mz[4][1] or mz [3][3]


def test_repair():
    mz = [[True, True, True, True, True],
          [True, False, False, False, False],
          [True, True, True, True, True],
          [True, False, True, False, False],
          [True, True, True, True, True]]
    mz = maze.repair(mz)
    assert not mz[3][0] or not mz[3][2]


def test_update_fog():
    mz = Maze(size=5)
    mz_rect = Rect(0, 0, mz.tile_px * 7, mz.tile_px * 7)
    fog = FogLayer(mz)
    for row in fog.fog:
        print(row)
    player = Player()
    fog.update_fog(player)
    for row in fog.fog:
        print(row)


def test_fog_rects():
    mz = Maze(size=5)
    mz_rect = Rect(0, 0, mz.tile_px * 7, mz.tile_px * 7)
    fog = FogLayer(mz)
    assert len(fog.fog) == 7
    assert len(fog.fog[0]) == 7
    assert mz.tile_px == fog.px
    rects = fog.fog_rects(mz_rect)
    assert len(rects) == 7
    assert len(rects[0]) == 7
    assert type(rects[0][0][0]) == Rect
    assert type(rects[0][0][1]) == Color
    assert rects[0][0][0] == Rect(0, 0, mz.tile_px, mz.tile_px)
    assert rects[0][0][1] == Color('black')
    assert rects[0][0][1].a == 255

