from queue import PriorityQueue


def dijkstra(grid, start, end, draw):
    nodes_to_explore = PriorityQueue()
    path_nodes = {}
    visited_nodes = set()
    node_index = 0

    nodes_to_explore.put((0, node_index, start))

    distance = {node: float("inf") for row in grid.grid for node in row}
    distance[start] = 0

    while not nodes_to_explore.empty():
        current_node = nodes_to_explore.get()[2]

        if current_node != start and current_node != end:
            current_node.visit_node()

        for neighbor in current_node.neighbours:
            temp_distance = distance[current_node] + 1

            if temp_distance < distance[neighbor]:
                path_nodes[neighbor] = current_node
                distance[neighbor] = temp_distance

            if neighbor not in visited_nodes:
                node_index += 1
                nodes_to_explore.put((distance[neighbor], node_index, neighbor))
                visited_nodes.add(neighbor)

                if neighbor != end and neighbor != start:
                    neighbor.make_available()

        draw()
    if end not in path_nodes:
        return False

    reconstruct_path(path_nodes, end, draw)
    end.make_end()
    return True


def reconstruct_path(path_nodes, current_node, draw):
    print("Algorithm: Dijkstra\nPath\nStart:")
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
