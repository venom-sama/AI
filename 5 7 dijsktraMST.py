import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # If the graph is undirected

    def dijkstra(self, src):
        visited = [False] * self.V
        distance = [sys.maxsize] * self.V
        distance[src] = 0

        for _ in range(self.V):
            u = self.min_distance(distance, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and distance[v] > distance[u] + self.graph[u][v]
                ):
                    distance[v] = distance[u] + self.graph[u][v]

        self.print_solution(distance)

    def min_distance(self, distance, visited):
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if distance[v] < min_dist and not visited[v]:
                min_dist = distance[v]
                min_index = v

        return min_index

    def print_solution(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t {distance[node]}")

def display_menu():
    print("\nMenu:")
    print("1. Add an Edge")
    print("2. Find Shortest Paths (Dijkstra's Algorithm)")
    print("3. Quit")

def add_edge(graph):
    u = int(input("Enter the source vertex: "))
    v = int(input("Enter the destination vertex: "))
    w = int(input("Enter the weight of the edge: "))
    graph.add_edge(u, v, w)
    print(f"Edge ({u}, {v}) with weight {w} added to the graph.")

def find_shortest_paths(graph):
    source = int(input("Enter the source vertex: "))
    graph.dijkstra(source)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        
