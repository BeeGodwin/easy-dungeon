class Player:

    def __init__(self, x=1, y=1, sight_r=5):
        self.x = x
        self.y = y
        self.next_x = x
        self.next_y = y
        self.sight_r = sight_r

    def handle_input(self, ky):
        """Handles keyboard input."""
        if ky == 119:
            self.next_y -= 1
        elif ky == 115:
            self.next_y += 1
        elif ky == 97:
            self.next_x -= 1
        elif ky == 100:
            self.next_x += 1

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def update_pos(self):
        self.x = self.next_x
        self.y = self.next_y
