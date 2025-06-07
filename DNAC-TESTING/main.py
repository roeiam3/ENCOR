import subprocess
import sys
from dnac_client import get_token, get_topology
import networkx as nx
import matplotlib.pyplot as plt

def install_packages():
    try:
        import requests, networkx, matplotlib
    except ImportError:
        print("[!] Missing dependencies. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

install_packages()




def build_topology_graph(topology):
    G = nx.Graph()
    id_to_label = {node['id']: node['label'] for node in topology['nodes']}

    for link in topology['links']:
        src = id_to_label.get(link['source'])
        dst = id_to_label.get(link['target'])

        if src and dst:
            G.add_edge(src, dst)

    return G


def build_topology_graph(topology):
    G = nx.Graph()
    id_to_label = {node['id']: node['label'] for node in topology['nodes']}

    for link in topology['links']:
        src = id_to_label.get(link['source'])
        dst = id_to_label.get(link['target'])

        if src and dst:
            G.add_edge(src, dst)

    return G

def draw_and_save_graph(G, filename="topology.png"):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
    plt.title("Simplified Physical Topology from DNAC")
    plt.savefig(filename)
    print(f"[+] Topology image saved as {filename}")


def main():
    token = get_token()
    topology = get_topology(token)
    G = build_topology_graph(topology)
    draw_and_save_graph(G)

if __name__ == "__main__":
    main()

