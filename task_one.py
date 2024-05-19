import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Створимо граф, що моделює транспортну мережу міста
G = nx.Graph()

# Додамо вузли (станції)
stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(stations)

# Додамо ребра (шляхи між станціями) з вагами (наприклад, відстань в км)
edges = [
    ("A", "B", 5),
    ("A", "C", 10),
    ("B", "D", 3),
    ("C", "D", 1),
    ("C", "E", 4),
    ("D", "E", 6),
    ("D", "F", 8),
    ("E", "F", 2),
    ("F", "G", 7),
    ("E", "H", 12),
]

G.add_weighted_edges_from(edges)


def main():
    # Візуалізуємо граф
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=12,
        font_weight="bold",
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Transport Network of a City")
    plt.show()

    # Аналіз основних характеристик графа
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degree_centrality = nx.degree_centrality(G)

    df = pd.DataFrame(
        list(degree_centrality.items()), columns=["Node", "Degree Centrality"]
    )
    df = df.sort_values(by="Degree Centrality", ascending=False)

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("\nDegree Centrality:")
    print(df)


if __name__ == "__main__":
    main()
