from pkgs.data.graph import Graph

class BFS():
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = []
        self.queue = []
        self.result = []
