from pkgs.data.graph import Graph

class DFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = []
        self.visited_edges = []

    def dfs(self, start_node):
        if start_node not in self.graph.nodes:
            raise ValueError("The start node is not in the graph")

        self.visited = []
        self.visited_edges = []

        self._dfs_recursive(start_node)

        return {
            "visited_nodes": self.visited,
            "visited_edges": self.visited_edges
        }

    def _dfs_recursive(self, current_node):
        if current_node not in self.visited:
            self.visited.append(current_node)

            for edge in self.graph.edges:
                neighbor = None
                if edge[0] == current_node and edge[1] not in self.visited:
                    neighbor = edge[1]
                elif edge[1] == current_node and edge[0] not in self.visited:
                    neighbor = edge[0]

                if neighbor:
                    self.visited_edges.append(edge)
                    self._dfs_recursive(neighbor)
