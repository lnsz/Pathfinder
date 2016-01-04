import tile as t


class Grid:
    def __init__(self, window, length, height, start, end):
        self.length = length
        self.height = height
        self.start = (start[0], start[1])
        self.end = (end[0], end[1])
        self.tiles = []
        for y in range(height):
            self.tiles.append([])
            for x in range(length):
                self.tiles[y].append(t.Tile(x, y, window.getWidth() // self.length, window.getHeight() // height))
        self.tiles[start[1]][start[0]].set_value("S")
        self.tiles[end[1]][end[0]].set_value("E")

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

    def tile_at(self, x, y):
        return self.tiles[y][x].get_value()

    def modify_tile(self, x, y, value):
        self.tiles[y][x].set_value(value)

    def get_tiles(self):
        return self.tiles

        return self.length

    def get_height(self):
        return self.height

    def get_start(self):
        return self.start

    def get_end(self):
        return self.start

    def modify_tile(self, x, y, value):
        self.tiles[y][x].set_state(value)
