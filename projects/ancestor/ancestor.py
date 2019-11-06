class Stack:
    def __init__(self):
        self.stack = []

    def push(self, int):
        self.stack.append(int)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        else: 
            return None

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertice(self, int):
        if not int in self.vertices:
            self.vertices[int] = set()

    def add_edge(self, int1, int2):
        if int1 in self.vertices and int2 in self.vertices:
            self.vertices[int2].add(int1)

        else:
            raise KeyError("Key doesn't exist")

    def dfs(self, node):
        s = Stack()
        s.push(node)

        visited = set()

        while len(s.stack) > 0:
            v = s.pop()
        
            if not v in visited:
                visited.add(v)

                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

        if v == node:
            return -1
        else:
            return v


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for (parent, child) in ancestors:
        graph.add_vertice(parent)
        graph.add_vertice(child)
        graph.add_edge(parent, child)

    return graph.dfs(starting_node)

