import networkx as nx
import pylab as plt

class GraphParser():
    def __init__(self, path):
        self.path = path
        self.graphs = []

    def parseGraphs(self):
        with open(self.path) as f:
            for line in f.readlines():
                g = nx.DiGraph()
                split = line.split(",")
                for i in range(len(split) - 1):
                    g.add_edge(split[i], split[i + 1])
                
                self.graphs.append(g)


def test():
    parser = GraphParser("./dataset/graphs.csv")
    parser.parseGraphs()
    for graph in parser.graphs:
        nx.draw_networkx(graph, with_labels=True)
        plt.show()

if (__name__ == "__main__"):
    test()
