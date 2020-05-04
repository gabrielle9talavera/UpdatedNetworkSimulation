import unittest
import networkx as nx
from Path import Path
from NodeFailure import NodeFailure


class TestPathMethods(unittest.TestCase):

    def setUp(self):
        self.node_fail = NodeFailure()
        self.path = Path(self.node_fail)
        self.g = nx.Graph()
        self.g.add_nodes_from([1, 2, 3, 4, 5])

    def test_find_path_direct(self):
        self.g.add_edge(1, 3)
        self.path.find_path(self.g, 1, 3)
        self.assertEqual(self.path.path, [1, 3])

    def test_find_path_multi(self):
        self.g.add_edges_from([(1, 2), (2, 5), (1, 3), (3, 5)])
        self.path.find_path(self.g, 1, 5)
        self.assertEqual(self.path.path, [1, 2, 5])

    def test_find_path_shortest(self):
        self.g.add_weighted_edges_from([(1, 2, 1), (2, 5, 3), (1, 3, 1), (3, 5, 2)])
        self.path.find_path(self.g, 1, 5)
        self.assertEqual(self.path.path, [1, 3, 5])

    def test_find_dpath(self):
        self.g.add_edge(1, 5)
        self.path.find_path(self.g, 1, 5)
        self.assertEqual(self.path.dpath, [1, 5])

    def test_find_bfpath(self):
        self.g.add_edge(1, 2)
        self.path.find_path(self.g, 1, 2)
        self.assertEqual(self.path.bfpath, [1, 2])

    def test_find_path_none(self):
        self.g.add_edge(1, 3)
        self.path.find_path(self.g, 1, 5)
        self.assertEqual(self.path.path, [])

    def test_find_dpath_none(self):
        self.g.add_edge(1, 5)
        self.path.find_path(self.g, 1, 3)
        self.assertEqual(self.path.dpath, [])

    def test_find_bfpath_none(self):
        self.g.add_edge(1, 2)
        self.path.find_path(self.g, 1, 3)
        self.assertEqual(self.path.bfpath, [])

    def test_update(self):
        node_num = self.g.number_of_nodes()
        self.node_fail.fail_prob = .99
        self.node_fail.node_probs = [.2, .3, .1, .4, .5]
        self.path.update(self.g, 5, 1, 5)
        self.assertNotEqual(node_num, self.g.number_of_nodes())

    def test_find_get_cost(self):
        self.g.add_weighted_edges_from([(1, 3, 1), (3, 5, 2)])
        self.path.find_path(self.g, 1, 5)
        self.path.get_cost(self.g, 1, 5)
        self.assertEqual(self.path.cost, 3)

    def test_find_get_dcost(self):
        self.g.add_weighted_edges_from([(1, 3, 1), (3, 5, 2)])
        self.path.find_path(self.g, 1, 5)
        self.path.get_cost(self.g, 1, 5)
        self.assertEqual(self.path.dcost, 3)

    def test_find_get_bfcost(self):
        self.g.add_weighted_edges_from([(1, 3, 1), (3, 5, 2)])
        self.path.find_path(self.g, 1, 5)
        self.path.get_cost(self.g, 1, 5)
        self.assertEqual(self.path.bfcost, 3)


if __name__ == '__main__':
    unittest.main()
