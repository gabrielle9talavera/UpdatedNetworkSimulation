import random
import numpy as np


class NodeFailure(object):

    def __init__(self):
        self.fail_prob = -1
        self.failure = []
        self.node_probs = []

    # this gets a user input of the probability of node failure
    # returns a float which is the probability of failure
    def node_failure(self):
        while self.fail_prob < 0 or self.fail_prob > 1:
            text = input("Enter probability of node failure (0-1): ")
            self.fail_prob = float(text)

    # randomly generates a list of the probability of each node failing
    def find_node_probs(self, node_amount):
        self.node_probs = np.random.rand(node_amount)

    # this is to calculate which nodes are failing
    # parameters: nodeAmount = amount of nodes
    #            src = starting node
    #            dest = ending node
    # returns a list of the nodes that failed
    def calculate_failure(self, node_amount, src):
        # calculates the amount of nodes that can fail
        fail_amount = round(self.fail_prob / (1 / node_amount))

        # this randomly generates the nodes that could fail
        holder = {random.randint(0, node_amount) for x in range(0, fail_amount)}

        # this goes through the nodes that could fail and if their probability is lower than the failProb, then the node
        # will be added to the fail list
        for x in holder:
            if self.node_probs[x-1] < self.fail_prob and x != src:
                self.failure.append(x)
