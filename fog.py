from maze import Maze
from player import Player
from pygame import Color, Rect


class FogLayer:
    """A 2d array of integer values between 0 and 255 inclusive.
    Has methods which return an array of rects ready for drawing."""

    def __init__(self, mz: Maze):
        self.fog = [[255 for _ in range(mz.size + 2)] for _ in range(mz.size + 2)]
        self.seen = [[False for _ in range(mz.size + 2)] for _ in range(mz.size + 2)]
        self.seen_lvl = 192
        self.px = mz.tile_px
        self.reveal = [[False for _ in range(mz.size + 2)] for _ in range(mz.size + 2)]
        self.col = Color('black')

    def fog_rects(self, mz_rect):
        """Returns a 2d array of (rect, color) tuples."""
        fog_rects = []
        for y in range(len(self.fog)):
            row = []
            for x in range(len(self.fog[0])):
                top = mz_rect.top + y * self.px
                left = mz_rect.left + x * self.px
                fog_tile = Rect(left, top, self.px, self.px)
                col = self.col
                col.a = self.fog[y][x]
                row.append((fog_tile, col))
            fog_rects.append(row)
        return fog_rects

    def update_fog(self, p: Player):
        """Sets fog alpha values."""
        # print('Player at ({}, {}).'.format(p.x, p.y))
        for y in range(len(self.fog)):
            for x in range(len(self.fog[0])):
                xdiff = abs(x - p.x)
                ydiff = abs(y - p.y)
                diff = xdiff + ydiff
                if ydiff <= p.sight_r and xdiff <= p.sight_r and diff <= p.sight_r:
                    step = 255 // p.sight_r  # TODO make it circular, not diamond?
                    self.fog[y][x] = 0 + step * (diff - 1)
                    self.seen[y][x] = True
                    if self.fog[y][x] > self.seen_lvl:
                        self.fog[y][x] = self.seen_lvl
                else:
                    if self.seen[y][x]:
                        self.fog[y][x] = self.seen_lvl
                self.fog[p.y][p.x] = 0
