import pygame
from grid import Grid
WIDTH = 800
HEIGHT = 800

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Visual Search Algorithms")

if __name__ == "__main__":
    grid = Grid()

    start = None
    end = None

    run = True
    started = False

    while run:
        grid.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_position(mouse_pos)
                node = grid.grid[row][col]

                if not start:
                    start = node
                    node.make_start()
                elif not end and node != start:
                    end = node
                    node.make_end()
                elif node != start and node != end:
                    node.make_obstacle()
            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()
