import unittest

from backend.pkgs.data.graph import Graph
from backend.pkgs.helpers.graph_reader import read_graph_from_txt_file, read_lines

class TestGraphReader(unittest.TestCase):
    def test_graph_reader(self):
        graph = read_graph_from_txt_file("backend/tests/data/road-test-CA.txt")

        assert isinstance(graph, Graph)
        assert len(graph.nodes) == 945
        assert len(graph.edges) == 2081

    def test_read_lines(self):
        graph = read_lines("backend/tests/data/road-test-CA.txt")

        assert len(graph) == 2081

    def test_read_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            graph = read_graph_from_txt_file("file/not/exists.txt")
