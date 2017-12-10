from maze import Maze
from player import Player
from pygame import Color, Rect


class FogLayer:
    """A 2d array of integer values between 0 and 255 inclusive.
    Has methods which return an array of rects ready for drawing."""

    def __init__(self, mz: Maze):
        self.fog = [[255 for _ in range(mz.size + 2)] for _ in range(mz.size + 2)]
        self.px = mz.tile_px
        self.reveal = [[False for _ in range(mz.size + 2)] for _ in range(mz.size + 2)]
        self.col = Color('black')

    def fog_rects(self):
        """Returns a 2d array of (rect, color) tuples."""
        fog_rects = []
        return fog_rects

    def update_fog(self, p: Player):
        pass
