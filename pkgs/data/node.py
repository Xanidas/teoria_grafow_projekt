class Node:
    def __init__(self, label: str):
        self.label = label

    def __str__(self):
        return f"Node with label {self.label}"