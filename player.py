class Player:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def handle_input(self, ky):
        """Handles keyboard input."""
        if ky == 119:
            self.y -= 1
        elif ky == 115:
            self.y += 1
        elif ky == 97:
            self.x -= 1
        elif ky == 100:
            self.x += 1

    def set_pos(self, x, y):
        self.x = x
        self.y = y
