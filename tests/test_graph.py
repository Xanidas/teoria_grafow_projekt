import unittest
from pkgs.data.graph import Graph
from pkgs.data.node import Node

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        node_a = Node(label="A")
        self.graph.add_node(node_a)
        self.assertIn(node_a, self.graph.nodes)
        self.assertEqual(len(self.graph.nodes), 1)

    def test_get_node(self):
        node_a = Node(label="A")
        self.graph.add_node(node_a)
        node = self.graph.get_node("A")
        self.assertEqual(node.label, "A")

    def test_get_non_existent_node(self):
        node = self.graph.get_node("A")
        self.assertIsNone(node)

    def test_add_existing_node(self):
        node_a = Node(label="A")
        self.graph.add_node(node_a)
        self.graph.add_node(node_a)  # Add the same node again
        self.assertEqual(len(self.graph.nodes), 1)

    def test_remove_node(self):
        node_a = Node(label="A")
        self.graph.add_node(node_a)
        self.graph.remove_node(node_a)
        self.assertNotIn(node_a, self.graph.nodes)

    def test_remove_non_existent_node(self):
        node_a = Node(label="A")
        with self.assertRaises(ValueError):
            self.graph.remove_node(node_a)

    def test_add_edge_valid_nodes(self):
        node_a = Node(label="A")
        node_b = Node(label="B")
        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_edge(node_a, node_b)
        self.assertIn((node_a, node_b), self.graph.edges)

    def test_add_edge_invalid_nodes(self):
        node_a = Node(label="A")
        node_b = Node(label="B")
        with self.assertRaises(ValueError):
            self.graph.add_edge(node_a, node_b)  # Nodes not in graph

    def test_graph_string_representation(self):
        node_a = Node(label="A")
        node_b = Node(label="B")
        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.assertEqual(str(self.graph), "Graph with 2 nodes and 0 edges")
