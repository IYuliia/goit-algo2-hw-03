import networkx as nx
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def build_graph():
    G = nx.DiGraph()

    edges = [
        ('T1', 'S1', 25), ('T1', 'S2', 20), ('T1', 'S3', 15),
        ('T2', 'S3', 15), ('T2', 'S4', 30), ('T2', 'S2', 10),
        ('S1', 'M1', 15), ('S1', 'M2', 10), ('S1', 'M3', 20),
        ('S2', 'M4', 15), ('S2', 'M5', 10), ('S2', 'M6', 25),
        ('S3', 'M7', 20), ('S3', 'M8', 15), ('S3', 'M9', 10),
        ('S4', 'M10', 20), ('S4', 'M11', 10), ('S4', 'M12', 15),
        ('S4', 'M13', 5), ('S4', 'M14', 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    G.add_node('SuperSource')
    G.add_node('SuperSink')

    G.add_edge('SuperSource', 'T1', capacity=float('inf'))
    G.add_edge('SuperSource', 'T2', capacity=float('inf'))

    stores = [f'M{i}' for i in range(1, 15)]
    for store in stores:
        G.add_edge(store, 'SuperSink', capacity=float('inf'))

    return G

def visualize_graph(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    labels = {(u, v): G[u][v]['capacity'] for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Logistics Flow Network")
    plt.show()

def compute_max_flow(G):
    flow_value, flow_dict = nx.maximum_flow(G, 'SuperSource', 'SuperSink')
    return flow_value, flow_dict

def build_flow_table(flow_dict):
    table = PrettyTable()
    table.field_names = ["Terminal", "Store", "Actual flow (units)"]

    for terminal in ["T1", "T2"]:
        for storage, flow in flow_dict[terminal].items():
            if isinstance(flow, dict):  
                for shop, shop_flow in flow.items():
                    if shop_flow > 0: 
                        table.add_row([terminal, shop, shop_flow])
            elif flow > 0:
                table.add_row([terminal, storage, flow])

    return table

def analyze_results(flow_dict, G):
    print("\n1. Terminals with the highest total flow:")
    terminal_flows = {}

    for terminal, storages in flow_dict.items():
        total_flow = sum(flow for flow in storages.values())
        terminal_flows[terminal] = total_flow

    max_terminal = max(terminal_flows, key=terminal_flows.get)
    print(f"   - {max_terminal} provides the highest flow: {terminal_flows[max_terminal]} units")

    print("\n2. Routes with the smallest capacity (potential bottlenecks):")
    min_capacity_edges = sorted([(u, v, G[u][v]['capacity']) for u, v in G.edges()], key=lambda x: x[2])[:3]
    for u, v, capacity in min_capacity_edges:
        print(f"   - Route {u} -> {v} has a capacity of {capacity} units.")

    store_flows = {}
    for storage, flows in flow_dict.items():
        for store, flow in flows.items():
            if flow > 0:
                store_flows[store] = store_flows.get(store, 0) + flow 

    if store_flows: 
        min_store = min(store_flows, key=store_flows.get)
        print("\n3. Stores receiving the least goods:")
        print(f"   - {min_store} received the lowest flow: {store_flows[min_store]} units")
    else:
        print("\n3. No stores received any goods.")

    print("\n4. Potential bottlenecks to improve:")
    for u, v, cap in min_capacity_edges:
        if cap < 10:
            print(f"   - Consider increasing capacity on {u} → {v}")

def main():
    G = build_graph()
  
    visualize_graph(G)
    
    max_flow, flow_dict = compute_max_flow(G)
    
    print(f"\nMaximum Flow: {max_flow} units\n")
    
    table = build_flow_table(flow_dict)
    print(table)

    analyze_results(flow_dict, G)

if __name__ == "__main__":
    main()

    
