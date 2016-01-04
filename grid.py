import tile as t


class Grid:
    def __init__(self, length, height, start, end):
        self.length = length
        self.height = height
        self.start = (start[0], start[1])
        self.end = (end[0], end[1])
        self.tiles = []
        for x in range(length):
            self.tiles.append([])
            for y in range(height):
                self.tiles[x].append(t.Tile(x, y))
        self.tiles[start[1]][start[0]].set_state("start")
        self.tiles[end[1]][end[0]].set_state("end")

    def __str__(self):
        s = ""
        for x in self.tiles:
            for y in x:
                s += str(y)
                s += "\t"
            s += "\n"
        return s

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_start(self):
        return self.start

    def get_end(self):
        return self.start

    def modify_tile(self, x, y, value):
        self.tiles[y][x].set_state(value)
