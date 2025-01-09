from typing import List, Tuple
from pydantic import BaseModel, Field
from pkgs.data.node import Node

class Graph(BaseModel):
    nodes: List[Node] = Field(default_factory=list)
    edges: List[Tuple[Node, Node]] = Field(default_factory=list)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def get_node(self, label: str):
        for node in self.nodes:
            if node.label == label:
                return node
        return None

    def remove_node(self, node):
        if node not in self.nodes:
            raise ValueError("Node not in the graph")
        self.nodes.remove(node)

    def add_edge(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("One or both of the nodes are not in the graph")
        self.edges.append((node1, node2))

    def __str__(self) -> str:
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"
