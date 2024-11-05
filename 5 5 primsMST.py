import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim_mst(self):
        key = [float("inf")] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def min_key(self, key, mst_set):
        min_val = float("inf")
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

def print_mst(graph, parent):
    print("Edge \tWeight")
    for i in range(1, graph.V):
        print(f"{parent[i]} - {i} \t{graph.graph[i][parent[i]]}")

def main():
    while True:
        print("\nPrim's Minimal Spanning Tree Algorithm Menu:")
        print("1. Create Graph")
        print("2. Find MST")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vertices = int(input("Enter the number of vertices: "))
            g = Graph(vertices)

            while True:
                edge_info = input("Enter an edge (u v w), or 'q' to finish: ")
                if edge_info == 'q':
                    break
                u, v, w = map(int, edge_info.split())
                g.add_edge(u, v, w)

        elif choice == "2":
            if 'g' in locals():
                parent = g.prim_mst()
                print_mst(g, parent)
            else:
                print("Please create a graph first.")
                
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
