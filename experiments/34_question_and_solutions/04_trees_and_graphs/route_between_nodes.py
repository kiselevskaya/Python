# route_between_nodes.py


from collections import defaultdict
import queue


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)

    def add_edge(self, _from, _to):
        self.graph[_from].append(_to)

    def get_graph(self):
        print(self.graph)


class SearchPath:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.visited = []
        self.q = queue.Queue()

    def visited(self, node):
        if node in self.visited:
            return True
        self.visited.append(node)
        return False

    def enqueue(self, node):
        for vertex in self.graph.graph[node]:
            if vertex == self.end:
                return True
            self.q.put(vertex)
        return False

    def path(self):
        self.q.put(self.start)
        while not self.q.empty():
            node = self.q.get()
            if not self.visited:
                if self.enqueue(node):
                    return True
        return False


if __name__ == '__main__':
    g = Graph(0)
    g.add_edge(0, 3)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.get_graph()
    start, end = 2, 3
    path_exist = SearchPath(g, start, end).path()
    print('There {} a route between nodes {} and {}'.format('is' if path_exist else "isn't", start, end))

    start, end = 3, 2
    path_exist = SearchPath(g, start, end).path()
    print('There {} a route between nodes {} and {}'.format('is' if path_exist else "isn't", start, end))
