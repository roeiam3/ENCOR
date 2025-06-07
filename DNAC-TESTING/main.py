from dnac_client import get_token, get_topology
import networkx as nx
import matplotlib.pyplot as plt

def build_topology_graph(topology):
    G = nx.Graph()
    id_to_label = {node['id']: node['label'] for node in topology['nodes']}

    for link in topology['links']:
        src = id_to_label.get(link['source'])
        dst = id_to_label.get(link['target'])
        src_intf = link.get('sourceInterfaceName', '')
        dst_intf = link.get('targetInterfaceName', '')
        label = f"{src_intf} ↔ {dst_intf}"

        if src and dst:
            G.add_edge(src, dst, label=label)

    return G

def draw_and_save_graph(G, filename="topology.png"):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)

    # Draw edge labels (interfaces)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Physical Topology from DNAC")
    plt.savefig(filename)
    print(f"[+] Topology with interfaces saved as {filename}")

def main():
    token = get_token()
    topology = get_topology(token)
    G = build_topology_graph(topology)
    draw_and_save_graph(G)

if __name__ == "__main__":
    main()
