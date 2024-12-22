class Graph:

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def __init__(self):
        self.nodes = []
        self.edges = []

    def __str__(self) -> str:
        return f"Graph with {len(self.nodes)} nodes"
