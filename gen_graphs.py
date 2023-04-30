import random as rand

maxGraphs = 1000

graphPossibilities = [f"P{10 * num}" for num in range(1, maxGraphs + 1)]

def generate_graps(amount: int):
    graphs = []
    for graph in range(amount):
        graphLen = rand.randint(0, len(graphPossibilities)//10)
        graph = []
        for _ in range(graphLen):
            node = graphPossibilities[rand.randint(0, len(graphPossibilities) - 1)]
            graph.append(node)
        graphs.append(graph)

    return graphs

def writeToCsv(path, graphs):
    writeString = ""
    for graph in graphs:
        for vertex in graph:
            writeString += vertex + ","
        writeString = writeString[:len(writeString) - 1]
        writeString += "\n"
    with open(path, "w") as f:
        f.write(writeString)


def test():
    graphs = generate_graps(10)
    writeToCsv("./dataset/graphs.csv", graphs)



if (__name__ == "__main__"):
    test()

