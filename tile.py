class Tile:

    def __init__(self, wall=False, px=32, col=(200, 200, 150)):

        self.wall = wall
        self.px = px
        self.col = col

    def __eq__(self, other):
        if type(self) == type(other):
            return True
        return False


class Wall(Tile):

    def __init__(self, px=32):
        super().__init__(px=px)
        self.wall = True
        self.col = (32, 32, 0)
