import pygame
from grid import Grid
from astar import a_star
from dfs import dfs
from bfs import bfs
from ucs import ucs
from dijkstra import dijkstra
import colors

WIDTH = 750
HEIGHT = 750

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Search Algorithms")
grid = Grid()
current_algorithm = "None"

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
                if event.key == pygame.K_0:
                    start = None
                    end = None
                    grid.reset_grid()

                elif event.key == pygame.K_1 and not started:
                    current_algorithm = "A*"
                    started = True

                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)

                    if not a_star(grid, start, end, lambda: grid.draw(window)):
                        print("No path found using A* algorithm")
                    started = False

                elif event.key == pygame.K_2 and not started:
                    started = True

                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)

                    if not bfs(start, end, lambda: grid.draw(window)):
                        print("No path found using BFS algorithm")
                    started = False

                elif event.key == pygame.K_3 and not started:
                    started = True

                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)

                    if not dfs(start, end, lambda: grid.draw(window)):
                        print("No path found using DFS algorithm")
                    started = False

                elif event.key == pygame.K_4 and not started:
                    started = True

                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)

                    if not ucs(start, end, lambda: grid.draw(window)):
                        print("No path found using UCS algorithm")
                    started = False

                elif event.key == pygame.K_5 and not started:
                    started = True

                    for row in grid.grid:
                        for node in row:
                            grid.get_neighbours(node)

                    if not dijkstra(grid, start, end, lambda: grid.draw(window)):
                        print("No path found using Dijkstra's algorithm")
                    started = False

                elif event.key == pygame.K_t:
                    if grid.current_theme == colors.THEMES['default']:
                        grid.apply_theme('dark')
                    elif grid.current_theme == colors.THEMES['dark']:
                        grid.apply_theme('light')
                    else:
                        grid.apply_theme('default')

    pygame.quit()
