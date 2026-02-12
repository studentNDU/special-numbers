import networkx as nx
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

def get_amicable_graph(N):
    # Обчислюємо суму дільників для всіх чисел до N
    s = [1] * (N + 1)
    s[0] = 0
    for i in range(2, N // 2 + 1):
        for j in range(2 * i, N + 1, i):
            s[j] += i

    # Знаходимо пари дружніх чисел
    pairs = [(i, s[i]) for i in range(2, N + 1)
             if i < s[i] <= N and s[s[i]] == i]

    if not pairs:
        return None

    # Створюємо граф
    G = nx.Graph(pairs)

    # Візуалізація
    fig, ax = plt.subplots(figsize=(12, 8))
    pos = nx.spring_layout(G, k=1.5, seed=42)
    colors = ['skyblue' if n % 2 == 0 else 'lightcoral' for n in G.nodes()]
    nx.draw(G, pos, ax=ax, with_labels=True, node_color=colors, 
            node_size=1500, font_weight='bold', edge_color='gray', width=2)
    ax.set_title(f"Граф дружніх чисел (N = {N})\n"
                 f"Пар: {len(pairs)}, Вершин: {G.number_of_nodes()}",
                 fontsize=14, pad=20)
    ax.axis('off')
    plt.show()

    return G

# Виклик функції
get_amicable_graph(20000)
