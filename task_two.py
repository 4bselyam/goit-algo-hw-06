from task_one import G

start_node = "A"
end_node = "H"


def bfs_path(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == end:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def dfs_path(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    for next in set(graph.neighbors(start)) - set(path):
        result = dfs_path(graph, next, end, path + [next])
        if result is not None:
            return result


def results():
    print(
        f"Shortest path from {start_node} to {end_node} using BFS: {bfs_path(G, start_node, end_node)}"
    )
    print(
        f"Shortest path from {start_node} to {end_node} using DFS: {dfs_path(G, start_node, end_node)}"
    )


if __name__ == "__main__":
    results()
