import unittest
from unittest import mock
from NodeFailure import NodeFailure


class TestNodeFailureMethods(unittest.TestCase):

    def setUp(self):
        self.node_fail = NodeFailure()

    @mock.patch('NodeFailure.input', create=True)
    def test_node_failure_in_range(self, mocked_input):
        mocked_input.side_effect = [.3]
        self.node_fail.node_failure()
        self.assertEqual(self.node_fail.fail_prob, .3)

    @mock.patch('NodeFailure.input', create=True)
    def test_node_failure_out_range(self, mocked_input):
        mocked_input.side_effect = [2, -2, .2]
        self.node_fail.node_failure()
        self.assertEqual(self.node_fail.fail_prob, .2)

    def test_find_node_probs(self):
        self.node_fail.find_node_probs(5)
        self.assertEqual(len(self.node_fail.node_probs), 5)

    def test_calculate_failure_low_prob(self):
        self.node_fail.fail_prob = .2
        self.node_fail.node_probs = [.5, .6, .3, .7, .4]
        self.node_fail.calculate_failure(5, 2)
        self.assertEqual(self.node_fail.failure, [])

    def test_calculate_failure_zero_prob(self):
        self.node_fail.fail_prob = 0
        self.node_fail.node_probs = [.5, .6, .3, .7, .4]
        self.node_fail.calculate_failure(5, 2)
        self.assertEqual(self.node_fail.failure, [])

    def test_calculate_failure_high_prob(self):
        self.node_fail.fail_prob = .8
        self.node_fail.node_probs = [.2, .3, .1, .4, .5]
        self.node_fail.calculate_failure(5, 3)
        self.assertNotEqual(self.node_fail.failure, [])


if __name__ == '__main__':
    unittest.main()
