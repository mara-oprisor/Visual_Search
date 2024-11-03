from node import Node
import pygame
import colors

ROWS = 50
WIDTH = 750
GREY = (64, 224, 208)


class Grid:
    def __init__(self):
        self.rows = ROWS
        self.width = WIDTH
        self.node_width = self.width // self.rows
        self.current_theme = colors.THEMES["default"]
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []

        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                node = Node(i, j, self.node_width, self.current_theme)
                grid[i].append(node)

        return grid

    def reset_grid(self):
        for row in self.grid:
            for node in row:
                node.reset(self.current_theme)

    def draw_grid_lines(self, window):
        for i in range(self.rows):
            pygame.draw.line(window, GREY, (0, i * self.node_width), (self.width, i * self.node_width))
            for j in range(self.rows):
                pygame.draw.line(window, GREY, (j * self.node_width, 0), (j * self.node_width, self.width))

    def draw(self, window):
        window.fill(self.current_theme["default"])

        for row in self.grid:
            for node in row:
                pygame.draw.rect(window, node.color, (node.x, node.y, node.width, node.width))

        self.draw_grid_lines(window)
        pygame.display.update()

    def get_clicked_position(self, mouse_pos):
        y, x = mouse_pos
        row = y // self.node_width
        col = x // self.node_width

        return row, col

    def get_neighbours(self, node):
        neighbours = []
        if node.row < self.rows - 1 and not self.grid[node.row + 1][node.col].is_obstacle():
            neighbours.append(self.grid[node.row + 1][node.col])

        if node.col > 0 and not self.grid[node.row][node.col - 1].is_obstacle():
            neighbours.append(self.grid[node.row][node.col - 1])

        if node.row > 0 and not self.grid[node.row - 1][node.col].is_obstacle():
            neighbours.append(self.grid[node.row - 1][node.col])

        if node.col < self.rows - 1 and not self.grid[node.row][node.col + 1].is_obstacle():
            neighbours.append(self.grid[node.row][node.col + 1])

        node.neighbours = neighbours

    def apply_theme(self, theme_name):
        self.current_theme = colors.THEMES[theme_name]
        for row in self.grid:
            for node in row:
                node.reset(self.current_theme)
