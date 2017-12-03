from tile import *


class Maze:
    """the game board. Essentially a 2D array of tiles."""

    def __init__(self, size=17, tilepx=32):
        self.size = size  # tiles square. Should be odd.
        self.tilepx = tilepx
        self.maze = self.make_maze()

    def make_maze(self):
        """returns a maze ready for play. PH code here!"""
        init_maze = self.init_maze()
        maze = []
        for row in init_maze:
            pass  # straight copy of the first 'wall' row to maze
            # then make 2 'rooms' in the next row
        return init_maze

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

    def room_count(self, maze):
        """Counts rooms. Takes a 2d maze array. Doesn't use attrs because
        that way it can be sent an arbitrary subsection of the array."""
        n = 0
        bools = []
        for y in range(len(maze)):
            bool_row = []
            for x in range(len(maze[0])):
                if type(self.maze[y][x]) == Wall:
                    bool_row.append(False)
                else:
                    bool_row.append(True)  # true means it's a room / path
            bools.append(bool_row)
        for y in range(self.size):
            for x in range(self.size):
                if bools[y][x]:
                    n += 1
                    self.flood_fill(bools, x, y)
        return n

    def flood_fill(self, bools, x, y):
        """for the cell with value True at x, y in 2D array bools, first
         mark it False, and if adjacent cells are True, call flood_fill
         on them also. We've effectively filled a 'room'."""
        bools[y][x] = False
        for (x_2, y_2) in self.get_adj_tiles(x, y):
            if bools[y_2][x_2]:
                self.flood_fill(bools, x_2, y_2)

    def get_adj_tiles(self, x, y):
        """returns a list of (x, y) tuples describing adjacent coordinates.
        Respects the edge of the board and corners."""
        size = self.size - 1
        lst = []
        if y > 0:
            lst.append((x, y - 1))
        if x > 0:
            lst.append((x - 1, y))
        if x < size:
            lst.append((x + 1, y))
        if y < size:
            lst.append((x, y + 1))
        return lst
