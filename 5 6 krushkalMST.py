class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []

        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

def display_menu():
    print("\nMenu:")
    print("1. Add an Edge")
    print("2. Find Minimum Spanning Tree (Kruskal's Algorithm)")
    print("3. Quit")

def add_edge(graph):
    u = int(input("Enter the source vertex: "))
    v = int(input("Enter the destination vertex: "))
    w = int(input("Enter the weight of the edge: "))
    graph.add_edge(u, v, w)
    print(f"Edge ({u}, {v}) with weight {w} added to the graph.")

def find_minimum_spanning_tree(graph):
    minimum_spanning_tree = graph.kruskal_mst()
    print("\nEdges in Minimum Spanning Tree:")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_edge(g)
        elif choice == '2':
            find_minimum_spanning_tree(g)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    main()
