import unittest
import networkx as nx
from Node import Node
from NodeFailure import NodeFailure
from Path import Path


class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.node = Node()
        self.node_fail = NodeFailure()
        self.path = Path(self.node_fail)
        self.g = nx.Graph()
        self.g.add_nodes_from([0, 1, 2, 3, 4])

    def test_direct_path(self):
        self.g.add_weighted_edges_from([(1, 2, 1), (2, 4, 3), (1, 3, 1), (3, 4, 2)])
        self.node.n = 5
        self.node.src = 1
        self.node.dest = 4
        self.path.find_path(self.g, self.node.src, self.node.dest)
        self.assertEqual(self.path.path, [1, 3, 4])

    def test_direct_path_w_update(self):
        self.g.add_weighted_edges_from([(1, 2, 1), (2, 4, 3), (1, 3, 1), (3, 4, 2)])
        self.node.n = 5
        self.node.src = 1
        self.node.dest = 4
        self.node_fail.fail_prob = 0
        self.node_fail.node_probs = [.2, .3, .1, .4, .5]
        self.path.find_path(self.g, self.node.src, self.node.dest)
        self.path.update(self.g, 5, self.node.src, self.node.dest)
        self.assertEqual(self.path.path, [1, 3, 4])

    def test_direct_path_cost(self):
        self.g.add_weighted_edges_from([(1, 2, 1), (2, 4, 3), (1, 3, 1), (3, 4, 2)])
        self.node.n = 5
        self.node.src = 1
        self.node.dest = 4
        self.node_fail.fail_prob = 0
        self.node_fail.node_probs = [.2, .3, .1, .4, .5]
        self.path.find_path(self.g, self.node.src, self.node.dest)
        self.path.update(self.g, 5, self.node.src, self.node.dest)
        self.path.get_cost(self.g, self.node.src, self.node.dest)
        self.assertEqual(self.path.cost, 3)


if __name__ == '__main__':
    unittest.main()
