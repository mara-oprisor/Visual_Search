import pygame

WIDTH = 800
HEIGHT = 800


class Screen:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Visual Search Algorithms")

