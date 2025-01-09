class Graph:

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def add_edge(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("One or both of the nodes are not in the graph")
        self.edges.append((node1, node2))

    def __init__(self):
        self.nodes = []
        self.edges = []

    def __str__(self) -> str:
        return f"Graph with {len(self.nodes)} nodes"
