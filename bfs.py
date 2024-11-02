from queue import Queue


def bfs(start, end, draw):
    nodes_to_explore = Queue()
    path_nodes = {}
    visited_nodes = set()

    nodes_to_explore.put(start)
    visited_nodes.add(start)

    while not nodes_to_explore.empty():
        current_node = nodes_to_explore.get()

        if current_node == end:
            reconstruct_path(path_nodes, end, draw)
            end.make_end()
            return True

        if current_node != start:
            current_node.visit_node()

        for neighbour in current_node.neighbours:
            if neighbour not in visited_nodes:
                visited_nodes.add(neighbour)
                nodes_to_explore.put(neighbour)
                path_nodes[neighbour] = current_node

                if neighbour != end:
                    neighbour.make_available()


def reconstruct_path(path_nodes, current_node, draw):
    while current_node in path_nodes:
        current_node = path_nodes[current_node]
        current_node.construct_path()
        draw()
