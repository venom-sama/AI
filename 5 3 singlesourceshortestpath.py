import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0

        min_heap = [(0, src)]

        while min_heap:
            dist_u, u = heapq.heappop(min_heap)

            if dist_u > distances[u]:
                continue

            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[v], v))

        return distances

def print_shortest_paths(distances, src):
    print("Shortest distances from source vertex", src)
    for i, dist in enumerate(distances):
        print(f"Vertex {i}: {dist}")

def main():
    while True:
        print("\nSingle-Source Shortest Path (Dijkstra's Algorithm) Menu:")
        print("1. Create Graph")
        print("2. Find Shortest Paths")
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
                src_vertex = int(input("Enter the source vertex: "))
                distances = g.dijkstra(src_vertex)
                print_shortest_paths(distances, src_vertex)
            else:
                print("Please create a graph first.")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
