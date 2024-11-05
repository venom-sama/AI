def dfs(graph, start_node):
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)
    return traversal_order

def bfs(graph, start_node):
    visited = set()
    traversal_order = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def main():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = {}

    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        neighbors = input(f"Enter neighbors of node {node} (space-separated): ").replace(",", "").split()
        graph[node] = neighbors

    # Identify and add missing nodes
    missing_nodes = []
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in graph:
                missing_nodes.append(neighbor)
                
    for node in missing_nodes:
        graph[node] = []  # Initialize missing nodes with an empty list

    start_node = input("Enter the start node: ")

    print("DFS Traversal Order:")
    print(dfs(graph, start_node))

    print("\nBFS Traversal Order:")
    print(bfs(graph, start_node))

if __name__ == "__main__":
    main()
