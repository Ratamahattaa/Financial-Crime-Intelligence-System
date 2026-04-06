import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def build_transaction_graph(df: pd.DataFrame) -> nx.DiGraph:
    G = nx.DiGraph()
    for _, row in df.iterrows():
        src = row.get("sender_id", None)
        dst = row.get("receiver_id", None)
        amount = row.get("amount", 0.0)
        if src and dst:
            G.add_edge(src, dst, amount=amount)
    return G


def draw_graph(G: nx.DiGraph):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    labels = nx.get_edge_attributes(G, "amount")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    plt.title("Transaction Graph")
    plt.tight_layout()
    plt.show()
