from queue import PriorityQueue


def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)


def a_star(grid, start, end, draw):
    nodes_to_explore = PriorityQueue()
    path_nodes = {}
    visited_nodes = set()
    node_index = 0

    nodes_to_explore.put((0, node_index, start))

    cost = {node: float("inf") for row in grid.grid for node in row}
    cost[start] = 0
    estimated_cost = {node: float("inf") for row in grid.grid for node in row}
    estimated_cost[start] = heuristic(start.get_pos(), end.get_pos())

    while not nodes_to_explore.empty():
        current_node = nodes_to_explore.get()[2]

        if current_node == end:
            reconstruct_path(path_nodes, end, draw)
            end.make_end()
            return True

        if current_node != start:
            current_node.visit_node()

        for neighbor in current_node.neighbours:
            temp_cost = cost[current_node] + 1

            if temp_cost < cost[neighbor]:
                path_nodes[neighbor] = current_node
                cost[neighbor] = temp_cost
                estimated_cost[neighbor] = temp_cost + heuristic(neighbor.get_pos(), end.get_pos())

                if neighbor not in visited_nodes:
                    node_index += 1
                    nodes_to_explore.put((estimated_cost[neighbor], node_index, neighbor))
                    visited_nodes.add(neighbor)

                    if neighbor != end and neighbor != start:
                        neighbor.make_available()

        draw()

    return False


def reconstruct_path(path_nodes, current_node, draw):
    print("Algorithm: A*\nPath\nStart:")
    list_of_nodes = []
    while current_node in path_nodes:
        current_node = path_nodes[current_node]
        current_node.construct_path()
        list_of_nodes.append((current_node.row, current_node.col))
        draw()

    list_of_nodes.reverse()
    for node in list_of_nodes:
        print(node)

    print("Goal")
    print(f"Path length: {len(list_of_nodes)} steps\n\n")
