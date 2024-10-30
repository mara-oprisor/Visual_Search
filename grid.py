from node import Node
import pygame

ROWS = 50
WIDTH = 800
GREY = (64, 224, 208)
WHITE = (255, 255, 255)


class Grid:
    def __init__(self):
        self.rows = ROWS
        self.width = WIDTH
        self.node_width = self.width // self.rows
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []

        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                node = Node(i, j, self.node_width, self.rows)
                grid[i].append(node)

        return grid

    def draw_grid_lines(self, window):
        for i in range(self.rows):
            pygame.draw.line(window, GREY, (0, i * self.node_width), (self.width, i * self.node_width))
            for j in range(self.rows):
                pygame.draw.line(window, GREY, (j * self.node_width, 0), (j * self.node_width, self.width))

    def draw(self, window):
        window.fill(WHITE)

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
