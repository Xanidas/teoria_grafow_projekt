import unittest
from pkgs.data.node import Node

class TestNode(unittest.TestCase):

    def test_node_label(self):
        node = Node(label="A")
        self.assertEqual(node.label, "A")

    def test_node_str(self):
        node = Node(label="A")
        self.assertEqual(str(node), "Node with label A")