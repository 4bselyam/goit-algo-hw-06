from task_one import G


# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    nodes = list(graph.nodes)

    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)

        if distances[current_node] == float("inf"):
            break

        for neighbor, data in graph[current_node].items():
            weight = data["weight"]
            alternative_route = distances[current_node] + weight
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes


# Функція для відновлення шляху
def get_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(start)
    path.reverse()
    return path


def main():
    # Знаходження найкоротшого шляху між всіма вершинами графа
    shortest_paths = {}
    for start_node in G.nodes:
        distances, previous_nodes = dijkstra(G, start_node)
        for end_node in G.nodes:
            if start_node != end_node:
                shortest_paths[(start_node, end_node)] = get_path(
                    previous_nodes, start_node, end_node
                )
    print("Shortest paths between all nodes:")
    print(shortest_paths)


if __name__ == "__main__":
    main()
