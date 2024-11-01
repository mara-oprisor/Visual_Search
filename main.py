import pygame
from grid import Grid
from astar import a_star

WIDTH = 800
HEIGHT = 800

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Visual Search Algorithms")

grid = Grid()

if __name__ == "__main__":
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

                if not start and node != end:
                    start = node
                    node.make_start()
                elif not end and node != start:
                    end = node
                    node.make_end()
                elif node != start and node != end:
                    node.make_obstacle()
            elif pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_position(mouse_pos)
                node = grid.grid[row][col]
                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)
                    if not a_star(grid, start, end, lambda: grid.draw(window)):
                        # Print msg
                        pass

    pygame.quit()
