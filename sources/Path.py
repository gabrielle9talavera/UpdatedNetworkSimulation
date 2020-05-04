import networkx as nx


class Path(object):

    def __init__(self, fail_object):
        self.node_fail = fail_object
        self.path = []
        self.dpath = []
        self.bfpath = []
        self.cost = 0
        self.bfcost = 0
        self.dcost = 0

    # this finds the shortest path using the Floyd-Warshall function which was imported from networkx
    # if you want to compare Floyd-Warshall with Dijkstra's uncomment lines: 107, 112, 122
    # if you want to compare Floyd-Warshall with Bellman-Ford uncomment lines: 108, 113, 123
    def find_path(self, graph, src, dest):
        # finds node predecessors using a function imported from networkx
        predecessors, _ = nx.floyd_warshall_predecessor_and_distance(graph)

        try:
            # finds the shortest path through the Floyd-Warshall algorithm by using a function imported from networkx
            self.path = nx.reconstruct_path(src, dest, predecessors)
            self.dpath = nx.dijkstra_path(graph, src, dest)
            self.bfpath = nx.bellman_ford_path(graph, src, dest)

        except:
            # Print to the terminal if no path exists.
            self.path = []
            self.dpath = []
            self.bfpath = []

    # this updates the path and graph based on the node failures
    def update(self, graph, node_amount, src, dest):

        # uses the calculateFailure to get the failed nodes
        self.node_fail.calculate_failure(node_amount, src)

        # removes the nodes that failed from the graph
        graph.remove_nodes_from(self.node_fail.failure)

        # finds the new shortest path
        self.find_path(graph, src, dest)

    # gets the total cost of path
    def get_cost(self, graph, src, dest):
        edges = 0
        for i in range(1, len(self.path)):
            edges += graph.edges[self.path[i - 1], self.path[i]]['weight']
        self.cost = edges
        self.dcost = nx.dijkstra_path_length(graph, src, dest)
        self.bfcost = nx.bellman_ford_path_length(graph, src, dest)

    def print_path(self, graph, src, dest):
        if not self.path:
            # Print to the terminal if no path exists.
            print("ERROR: No available path from source: node", src, "to destination: node", dest)

        else:
            # prints the shortest path
            print("Path:", self.path)
            # print("Dijkstra's Path:", self.dpath)
            # print("Bellman-Ford Path:", self.bfpath)

            # prints the number of hops from source to destination
            print("Number of Hops:", len(self.path) - 1)
            # print("Dijkstra's Number of Hops:", len(self.dpath)-1)
            # print("Bellman-Ford Number of Hops:", len(self.bfpath)-1)

            # gets the total cost
            self.get_cost(graph, src, dest)

            print("Total Cost:", self.cost)
            # print("Dijkstra's Total Cost:", self.dcost)
            # print("Bellman-Ford Total Cost:", self.bfcost)
            print()
