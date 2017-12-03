from tile import *


class Maze:
    """the game board. Essentially a 2D array of tiles."""

    def __init__(self, size=17, tilepx=32):
        self.size = size  # tiles square. Should be odd.
        self.tilepx = tilepx
        self.maze = self.make_maze()

    def make_maze(self):
        """returns a maze ready for play. PH code here!"""
        maze = self.init_maze()
        return maze

    def init_maze(self):
        """returns a 'blank' maze."""
        t_px, size = self.tilepx, self.size
        maze = [[Wall(px=t_px) for _ in range(size)] for _ in range(size)]
        cell_row = False
        cell_open = False
        for row in maze:
            if cell_row:
                for i in range(len(row)):
                    if cell_open:
                        row[i] = Tile(px=t_px)
                    cell_open = not cell_open
            cell_row = not cell_row
            cell_open = False
        return maze

    def room_count(self,):
        """Counts rooms."""
        n = 0
        bools = []
        for y in range(self.size):
            bool_row = []
            for x in range(self.size):
                if type(self.maze[y][x]) == Wall:
                    bool_row.append(False)
                else:
                    bool_row.append(True)  # true means it's a room / path
            bools.append(bool_row)
        for y in range(self.size):
            for x in range(self.size):
                if bools[y][x]:
                    n += 1
                    # TODO hook up flood fill here
        return n

    def flood_fill(self, bools, x, y):
        """for the cell with value True at x, y in 2D array bools, first
         mark it False, and if adjacent cells are True, call flood_fill
         on them also."""
        pass
    
    def get_adj_tiles(self, x, y):
        """returns a list of (x, y) tuples describing adjacent coordinates.
        Respects the edge of the board and corners."""
        pass

