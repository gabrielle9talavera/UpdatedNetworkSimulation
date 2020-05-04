import unittest
from unittest import mock
from Node import Node


class TestNodeMethods(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    @mock.patch('Node.input', create=True)
    def test_node_amount(self, mocked_input):
        mocked_input.side_effect = [3]
        self.node.node_amount()
        self.assertEqual(self.node.n, 3)

    @mock.patch('Node.input', create=True)
    def test_src_node_in_range(self, mocked_input):
        mocked_input.side_effect = [3]
        self.node.src_node(8)
        self.assertEqual(self.node.src, 3)

    @mock.patch('Node.input', create=True)
    def test_src_node_out_range(self, mocked_input):
        mocked_input.side_effect = [9, -2, 3]
        self.node.src_node(8)
        self.assertEqual(self.node.src, 3)

    @mock.patch('Node.input', create=True)
    def test_dest_node_in_range(self, mocked_input):
        mocked_input.side_effect = [7]
        self.node.dest_node(8)
        self.assertEqual(self.node.dest, 7)

    @mock.patch('Node.input', create=True)
    def test_dest_node_out_range(self, mocked_input):
        mocked_input.side_effect = [8, -1, 2]
        self.node.dest_node(8)
        self.assertEqual(self.node.dest, 2)


if __name__ == '__main__':
    unittest.main()
