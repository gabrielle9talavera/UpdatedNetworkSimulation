class Node(object):

    def __init__(self):
        self.n = 0
        self.src = -1
        self.dest = -1

    # this gets a user input of how many nodes that are wanted
    # returns an integer of the amount of nodes
    def node_amount(self):
        # An input is requested and stored in a variable
        text = input("Enter number of nodes: ")

        # Converts the string into a integer.
        self.n = int(text)

    # this gets a user input of the starting node
    # returns an integer which is the source node
    def src_node(self, node_amount):
        while self.src > (node_amount - 1) or self.src < 0:
            text = input("Enter source node (possible values from 0 to the number of nodes - 1): ")
            self.src = int(text)

    # this gets a user input of the ending node
    # returns an integer which is the destination node
    def dest_node(self, node_amount):
        while self.dest > (node_amount - 1) or self.dest < 0:
            text = input("Enter destination node (possible values from 0 to the number of nodes - 1): ")
            self.dest = int(text)
