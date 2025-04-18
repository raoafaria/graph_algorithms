from collections import defaultdict

# --------- Topological Sort ---------
class GraphTopoSort:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack


# --------- DFS ---------
class GraphDFS:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.V
        print("DFS traversal starting from node", start_vertex)
        self.dfs_util(start_vertex, visited)
        print()


# --------- Kruskal ---------
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True
        return False

def kruskal(n, edges):
    edges.sort()
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# --------- Menu Prompt ---------
def print_menu():
    print("\n=== Graph Algorithm Menu ===")
    print("1. Topological Sort")
    print("2. Depth-First Search (DFS)")
    print("3. Kruskal’s Minimum Spanning Tree (MST)")
    print("4. Exit")

def input_graph_directed():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    graph = GraphTopoSort(V)
    print("Enter each edge as 'u v' (from u to v):")
    for _ in range(E):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    return graph

def input_graph_dfs():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    graph = GraphDFS(V)
    print("Enter each edge as 'u v' (undirected or directed):")
    for _ in range(E):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    return graph

def input_graph_kruskal():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    edges = []
    print("Enter each edge as 'u v weight':")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    return V, edges

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1–4): ")

        if choice == '1':
            print("\n--- Topological Sort ---")
            graph = input_graph_directed()
            order = graph.topological_sort()
            print("Topological Order:", order)

        elif choice == '2':
            print("\n--- Depth-First Search (DFS) ---")
            graph = input_graph_dfs()
            start = int(input("Enter starting vertex for DFS: "))
            graph.dfs(start)

        elif choice == '3':
            print("\n--- Kruskal’s MST ---")
            V, edges = input_graph_kruskal()
            mst, weight = kruskal(V, edges)
            print("Edges in MST:", mst)
            print("Total weight of MST:", weight)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")

if __name__ == "__main__":
    main()
