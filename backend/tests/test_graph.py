import unittest
from pkgs.data.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        node_a = "A"
        self.graph.add_node(node_a)
        self.assertIn(node_a, self.graph.nodes)
        self.assertEqual(len(self.graph.nodes), 1)

    def test_add_existing_node(self):
        node_a = "A"
        self.graph.add_node(node_a)
        self.graph.add_node(node_a)  # Add the same node again
        self.assertEqual(len(self.graph.nodes), 1)

    def test_add_edge_valid_nodes(self):
        node_a = "A"
        node_b = "B"
        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_edge(node_a, node_b)
        self.assertIn((node_a, node_b), self.graph.edges)

    def test_graph_string_representation(self):
        node_a = "A"
        node_b = "B"
        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.assertEqual(str(self.graph), "Graph with 2 nodes and 0 edges")

    def test_merge_graph(self):
        node_a = "A"
        node_b = "B"
        node_c = "C"
        node_d = "D"

        graph1 = Graph()
        graph1.add_node(node_a)
        graph1.add_node(node_b)
        graph1.add_edge(node_a, node_b)

        graph2 = Graph()
        graph2.add_node(node_a)
        graph2.add_node(node_c)
        graph2.add_node(node_d)
        graph2.add_edge(node_a, node_c)
        graph2.add_edge(node_c, node_d)

        graph1.merge_graph(graph2)

        self.assertEqual(len(graph1.nodes), 4)
        self.assertEqual(len(graph1.edges), 3)
        self.assertIn((node_a, node_b), graph1.edges)
        self.assertIn((node_a, node_c), graph1.edges)
        self.assertIn((node_c, node_d), graph1.edges)
