class Tile:
    def __init__(self, x, y, state="empty"):
        self.x = x
        self.y = y
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def state_to_letter(self):
        if self.state == "empty":
            return "o"
        elif self.state == "wall":
            return "x"
        elif self.state == "start":
            return "S"
        elif self.state == "end":
            return "E"

    def __str__(self):
        return self.state_to_letter()
