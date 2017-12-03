class Tile:

    def __init__(self, wall=False, px=32, col=(200, 200, 150)):

        self.wall = wall
        self.px = px
        self.col = col

    # TODO define a base Tile class and extend through inheritance.
    # that might be as much as we need in terms of gameplay.
    # tiles can be a little bit like a FSM


class Wall(Tile):

    def __init__(self, px=32):
        super().__init__(px=px)
        self.wall = True
        self.col = (32, 32, 0)
