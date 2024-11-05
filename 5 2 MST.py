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
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

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

def print_mst(mst):
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")

def main():
    while True:
        print("\nMinimum Spanning Tree Menu:")
        print("1. Create Graph")
        print("2. Find MST (Kruskal's Algorithm)")
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
                mst = g.kruskal_mst()
                print_mst(mst)
            else:
                print("Please create a graph first.")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
