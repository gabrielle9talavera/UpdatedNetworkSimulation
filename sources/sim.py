#####################################################################################################################
# AUTHOR:
# Gabrielle Talavera
#
# DESCRIPTION: This project simulates a mesh network where nodes and links may fail. Nodes may fail intermittently,
# and as an input to the simulation, each node and link will have a certain probability to fail. When such failure
# occurs, the network must adapt and re-route to avoid the faulty node.
#
# RUNNING THE PROGRAM:
# 1. Make sure Python is installed preferrably 3.7.4
# 2. Make sure numpy and networkx packages are downloaded
# 3. Run the program using 'python sim.py'
#
# OUTPUT:
# - Original Path
# - Number of hops with no node failures
# - Total Cost of Path
# - Updates:
#   - Nodes that fail every cycle.
#   - Updated path from source node to destination node
#   - Number of hops (how many links it has to pass over)
#   - Total Cost of path (all the weights on links added up)
#   - If the Dijkstra and Bellman-Ford feature is activated, then the
#   path, hops, and total cost would be printed for these algorithms
######################################################################################################################
import networkx as nx
import random
from Node import Node
from NodeFailure import NodeFailure
from Path import Path


class Sim(object):
    def __init__(self):
        self.node = Node()
        self.node_fail = NodeFailure()
        self.path = Path(self.node_fail)

    # this generates the graph
    # Parameters: n = node amount (based on user input)
    # returns the graph (network)
    def generate_graph(self, n):
        # finds the max amount of edges that can exist
        max_edges = (n * (n - 1)) / 2

        # based on the max amount of edges, it randomizes a number of edges that our graph will have
        e = random.randint(n, max_edges)

        # this generates a random graph using the amount of nodes and edges
        g = nx.gnm_random_graph(n, e)

        # this randomly assigns weights to the edges
        for (u, v) in g.edges():
            g.edges[u, v]['weight'] = random.randint(1, 10)

        return g

    def run_sim(self):
        # get user inputs
        self.node.node_amount()
        self.node.src_node(self.node.n)
        self.node.dest_node(self.node.n)
        self.node_fail.node_failure()

        # randomly generates a list of the probability of each node failing
        self.node_fail.find_node_probs(self.node.n)

        # generates the graph
        g = self.generate_graph(self.node.n)

        # # finds the shortest path
        self.path.find_path(g, self.node.src, self.node.dest)
        self.path.print_path(g, self.node.src, self.node.dest)

        # automatically does one case of failed nodes, so user can see what happens
        print("Updates: ")
        self.path.update(g, self.node.n, self.node.src, self.node.dest)
        print("Nodes that failed: ", self.node_fail.failure)
        self.path.print_path(g, self.node.src, self.node.dest)
        #
        # will keep executing update until user enters a q
        q = ''
        while q != 'q':
            print('Enter q to exit, or enter any other key to continue to update the graph with failed nodes: ')
            q = input()
            if q != 'q':
                print("Updates: ")
                self.path.update(g, self.node.n, self.node.src, self.node.dest)
                print("Nodes that failed: ", self.node_fail.failure)
                self.path.print_path(g, self.node.src, self.node.dest)


if __name__ == "__main__":
    sim = Sim()
    sim.run_sim()
