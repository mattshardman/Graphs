class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, int):
        self.stack.append(int)

    def dequeue(self):
        if len(self.stack) > 0:
            return self.stack.pop(-1)
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

    def bfs(self, starting_node):
        q = Queue()
        q.enqueue([starting_node])

        max_path_length = 1

        earliest_ancestor = -1

        while len(q.stack) > 0:
            # dequeue the path
            path = q.dequeue()
            # get the last vert
            vert = path[-1]
            # if path is longer or equal and the value is smaller, or if the path is longer
            if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
                # set the earliest ancestor to the vert
                earliest_ancestor = vert
                # set the max path length to the len of the path
                max_path_length = len(path)
            # loop over each neighbor in the graphs vertices at index of vert
            for neighbor in self.vertices[vert]:
                # make a copy of the path
                path_copy = list(path)
                # append neighbor to the coppied path
                path_copy.append(neighbor)
                # then enqueue the copied path
                q.enqueue(path_copy)

        return earliest_ancestor


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for (parent, child) in ancestors:
        graph.add_vertice(parent)
        graph.add_vertice(child)
        graph.add_edge(parent, child)

    return graph.bfs(starting_node)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)