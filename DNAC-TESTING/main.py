import subprocess
import sys

def install_packages():
    try:
        import requests, networkx, matplotlib
    except ImportError:
        print("[!] Missing dependencies. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

install_packages()


from dnac_client import get_token, get_topology
import networkx as nx
import matplotlib.pyplot as plt

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

def main():
    token = get_token()
    topology = get_topology(token)
    G = build_topology_graph(topology)
    draw_and_save_graph(G)

if __name__ == "__main__":
    main()

