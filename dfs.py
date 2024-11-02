from queue import LifoQueue


def dfs(start, end, draw):
    nodes_to_explore = LifoQueue()
    visited_nodes = set()
    path_nodes = {}

    visited_nodes.add(start)
    nodes_to_explore.put(start)

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
                path_nodes[neighbour] = current_node
                nodes_to_explore.put(neighbour)

            if neighbour != end and neighbour != start:
                neighbour.make_available()

        draw()

    return False


def reconstruct_path(path_nodes, current_node, draw):
    while current_node in path_nodes:
        current_node = path_nodes[current_node]
        current_node.construct_path()
        draw()
