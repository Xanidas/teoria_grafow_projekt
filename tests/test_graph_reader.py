from pkgs.data.graph import Graph
from pkgs.helpers.graph_reader import read_graph_from_txt_file, read_lines

def test_graph_reader():
    graph = read_graph_from_txt_file("tests/data/road-test-CA.txt")

    assert isinstance(graph, Graph)
    assert len(graph.nodes) == 945
    assert len(graph.edges) == 2081

def test_read_lines():
    graph = read_lines("tests/data/road-test-CA.txt")

    assert len(graph) == 2081