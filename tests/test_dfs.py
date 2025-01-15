import unittest
from pkgs.data.graph import Graph
from pkgs.dfs.dfs import DFS

class TestDFS(unittest.TestCase):

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

    def test_dfs(self):
        dfs = DFS(self.graph)
        result = dfs.dfs("a")

        expected_nodes = {'a', 'd', 'b', 'h', 'e', 'i', 'f', 'c', 'g'}
        expected_edges = {('a', 'd'), ('b', 'd'), ('b', 'h'), ('h', 'e'), ('e', 'i'), ('d', 'f'), ('f', 'c'),
                          ('g', 'c')}

        self.assertEqual(result["visited_nodes"], expected_nodes, "Visited nodes do not match")
        self.assertEqual(len(result["visited_edges"]), len(expected_edges), "Number of edges do not match")
        self.assertEqual({node for edge in result["visited_edges"] for node in edge}, expected_nodes,
                         "Not all nodes are connected by the edges")

    def test_dfs_with_invalid_node(self):
        dfs = DFS(self.graph)
        with self.assertRaises(ValueError):
            dfs.dfs("z")