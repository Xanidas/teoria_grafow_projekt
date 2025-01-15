from time import time

from fastapi import FastAPI
from backend.pkgs.data.graph import Graph
from backend.pkgs.bfs.bfs import BFS
from backend.pkgs.dfs.dfs import DFS

app = FastAPI()

# Initialize an empty graph (it will get populated with POST requests)
graph = Graph()

@app.post("/bfs/")
def bfs(graph: Graph, start_node_label: str):
    """Perform a breadth-first search on the graph."""

    bfs = BFS(graph)
    start_time = time()
    result = {"bfs_result": bfs.bfs(start_node_label)}
    end_time = time()
    result["time"] = end_time - start_time

    return result

@app.post("/dfs/")
def dfs(graph: Graph, start_node_label: str):
    """Perform a depth-first search on the graph."""

    dfs = DFS(graph)
    start_time = time()
    result = {"dfs_result": dfs.dfs(start_node_label)}
    end_time = time()
    result["time"] = end_time - start_time

    return result
