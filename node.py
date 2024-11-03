class Node:
    def __init__(self, row, col, width, theme):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.theme = theme
        self.color = self.theme["default"]
        self.neighbours = []
        self.width = width

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == self.theme["visited"]

    def is_obstacle(self):
        return self.color == self.theme["obstacle"]

    def is_start(self):
        return self.color == self.theme["start"]

    def is_end(self):
        return self.color == self.theme["end"]

    def reset(self, theme):
        self.color = theme["default"]

    def visit_node(self):
        self.color = self.theme["visited"]

    def make_available(self):
        self.color = self.theme["available"]

    def make_obstacle(self):
        self.color = self.theme["obstacle"]

    def make_start(self):
        self.color = self.theme["start"]

    def make_end(self):
        self.color = self.theme["end"]

    def construct_path(self):
        self.color = self.theme["path"]

    def __lt__(self, other):
        return False
