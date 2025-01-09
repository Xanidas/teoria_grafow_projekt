import unittest
from pkgs.data.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node("A")
        self.assertIn("A", self.graph.nodes)
        self.assertEqual(len(self.graph.nodes), 1)

    def test_add_existing_node(self):
        self.graph.add_node("A")
        self.graph.add_node("A")
        self.assertEqual(len(self.graph.nodes), 1)

    def test_remove_node(self):
        self.graph.add_node("A")
        self.graph.remove_node("A")
        self.assertNotIn("A", self.graph.nodes)

    def test_remove_non_existent_node(self):
        with self.assertRaises(ValueError):
            self.graph.remove_node("A")

    def test_add_edge_valid_nodes(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_edge("A", "B")
        self.assertIn(("A", "B"), self.graph.edges)

    def test_add_edge_invalid_nodes(self):
        with self.assertRaises(ValueError):
            self.graph.add_edge("A", "B")

    def test_graph_string_representation(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.assertEqual(str(self.graph), "Graph with 2 nodes")
