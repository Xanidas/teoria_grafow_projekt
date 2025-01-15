from typing import Set, Tuple
from pydantic import BaseModel, Field


class Graph(BaseModel):
    nodes: Set[str] = Field(default_factory=set)
    edges: Set[Tuple[str, str]] = Field(default_factory=set)

    def add_node(self, node):
        self.nodes.add(node)


    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.edges.add((node1, node2))


    def merge_graph(self, graph):
        self.nodes.update(graph.nodes)
        self.edges.update(graph.edges)


    def __str__(self) -> str:
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"
