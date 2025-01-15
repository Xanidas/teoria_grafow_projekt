import os

from backend.pkgs.data.graph import Graph

def read_lines(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line or line.startswith('#'):
                continue
            from_node, to_node = line.split()
            lines.append((from_node, to_node))
    return lines

def read_graph_from_txt_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    lines = read_lines(file_path)

    graph = Graph()

    for line in lines:
        graph.add_edge(line[0], line[1])

    return graph
