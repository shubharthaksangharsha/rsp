from typing import Dict, List, Set
from collections import deque


class Graph:
    def __init__(self):
        self.graph: Dict[int, List[int]] = {}

    def add_vertex(self, v: int) -> None:
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u: int, v: int) -> None:
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u: int, v: int) -> None:
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def remove_vertex(self, v: int) -> None:
        if v not in self.graph:
            return

        for nbr in self.graph[v]:
            self.graph[nbr].remove(v)

        del self.graph[v]

    def search(self, val: int) -> bool:
        return val in self.graph

    def dfs_recursive(self, start: int) -> None:
        visited: Set[int] = set()

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            print(node, end=" ")
            for nbr in self.graph.get(node, []):
                dfs(nbr)

        dfs(start)
        print()

    def dfs_iterative(self, start: int) -> None:
        visited: Set[int] = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                for nbr in reversed(self.graph.get(node, [])):
                    stack.append(nbr)
        print()

    def bfs(self, start: int) -> None:
        visited: Set[int] = set()
        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()
            print(node, end=" ")
            for nbr in self.graph.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        print()

    def graph_length(self) -> int:
        return len(self.graph)

    def edge_count(self) -> int:
        total = 0
        for v in self.graph:
            total += len(self.graph[v])
        return total // 2

    def clear(self) -> None:
        self.graph.clear()


if __name__ == "__main__":
    g = Graph()

    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)]

    for u, v in edges:
        g.add_edge(u, v)

    g.dfs_recursive(1)
    g.dfs_iterative(1)
    g.bfs(1)

    print(g.search(5))
    print(g.graph_length(), g.edge_count())

    g.clear()
    print(g.graph_length())
