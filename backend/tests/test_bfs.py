import unittest
from backend.pkgs.data.graph import Graph
from backend.pkgs.bfs.bfs import BFS

class TestBFS(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

        self.graph.add_edge("a", "d")
        self.graph.add_edge("a", "b")
        self.graph.add_edge("b", "d")
        self.graph.add_edge("b", "h")
        self.graph.add_edge("b", "e")
        self.graph.add_edge("d", "e")
        self.graph.add_edge("h", "e")
        self.graph.add_edge("e", "i")
        self.graph.add_edge("d", "f")
        self.graph.add_edge("g", "c")
        self.graph.add_edge("f", "c")
        self.graph.add_edge("d", "g")
        self.graph.add_edge("d", "c")

    def test_bfs(self):
        bfs = BFS(self.graph)
        result = bfs.bfs("a")

        expected_nodes = {'a', 'd', 'b', 'e', 'f', 'g', 'c', 'h', 'i'}
        expected_edges = {('a', 'd'), ('a', 'b'), ('d', 'e'), ('d', 'f'), ('d', 'g'), ('d', 'c'), ('b', 'h'),
                          ('e', 'i')}

        self.assertEqual(result["visited_nodes"], expected_nodes, "Visited nodes do not match")
        self.assertEqual(len(result["visited_edges"]), len(expected_edges), "Number of edges do not match")
        self.assertEqual({node for edge in result["visited_edges"] for node in edge}, expected_nodes, "Not all nodes are connected by the edges")

    def test_bfs_with_invalid_node(self):
        bfs = BFS(self.graph)
        with self.assertRaises(ValueError):
            bfs.bfs("z")