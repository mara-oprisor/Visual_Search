from queue import PriorityQueue


def ucs(start, end, draw):
    nodes_to_explore = PriorityQueue()
    visited_nodes = set()
    path_nodes = {}

    nodes_to_explore.put((0, start))
    visited_nodes.add(start)
    cost = {start: 0}

    while not nodes_to_explore.empty():
        current_cost, current_node = nodes_to_explore.get()

        if current_node == end:
            reconstruct_path(path_nodes, end, draw)
            end.make_end()
            return True

        if current_node != start:
            current_node.visit_node()

        for neighbour in current_node.neighbours:
            temp_cost = current_cost + 1

            if (neighbour not in visited_nodes) and temp_cost < cost.get(neighbour, float('inf')):
                visited_nodes.add(current_node)
                path_nodes[neighbour] = current_node
                cost[neighbour] = temp_cost
                nodes_to_explore.put((temp_cost, neighbour))

                if neighbour != end and neighbour != start:
                    neighbour.make_available()

        draw()


def reconstruct_path(path_nodes, current_node, draw):
    print("Algorithm: Uniform Cost Search\nPath\nStart:")
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
