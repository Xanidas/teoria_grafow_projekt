from pkgs.data.graph import Graph


class BFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = set()
        self.queue = []
        self.visited_edges = set()

    def bfs(self, start_node):
        if start_node not in self.graph.nodes:
            raise ValueError("The start node is not in the graph")

        self.queue = [start_node]

        while self.queue:
            current_node = self.queue.pop(0)

            if current_node not in self.visited:
                self.visited.add(current_node)

                for edge in self.graph.edges:
                    neighbor = None
                    if edge[0] == current_node and edge[1] not in self.visited:
                        neighbor = edge[1]
                    elif edge[1] == current_node and edge[0] not in self.visited:
                        neighbor = edge[0]

                    if neighbor and neighbor not in self.queue:
                        self.queue.append(neighbor)
                        self.visited_edges.add(edge)

        return {
            "visited_nodes": self.visited,
            "visited_edges": self.visited_edges
        }
