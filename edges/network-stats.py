def read_file(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def load_network(filename):
    file_data = read_file(filename)
    file_data = file_data.splitlines()
    edges = []
    for edge in file_data:
        edge = edge.split(',')
        if edge[0] == '' or edge[1] == '': continue
        edges.append(edge)
    return edges[1:]

def get_degree(network):
    indegree  = {}
    outdegree = {}
    for edge in network:
        source = edge[0]
        target = edge[1]
        if source not in outdegree: outdegree[source]  = 1
        else:                       outdegree[source] += 1
        if target not in indegree:   indegree[target]  = 1
        else:                        indegree[target] += 1
        if source not in indegree:   indegree[source] = 0
        if target not in outdegree: outdegree[target] = 0
    return indegree, outdegree

def get_degree_distribution(indegree, outdegree):
    degree_distribution = {}
    for node in indegree:
        degree = indegree[node] + outdegree[node]
        if degree not in degree_distribution: degree_distribution[degree]  = 1
        else:                                 degree_distribution[degree] += 1
    return sorted(degree_distribution.items())

def print_degree_distribution(degree_distribution, filename=None):
    file = open(filename, 'w')
    print("degree distribution:")
    file.write("degree distribution:\n")
    for item in degree_distribution:
        print(f"{item[0]}:\t{item[1]}")
        file.write(f"{item[0]}:\t{item[1]}\n")
    print()
    return

def test():
    network = load_network("network.csv")
    indegree, outdegree = get_degree(network)
    degree_distribution = get_degree_distribution(indegree, outdegree)
    print_degree_distribution(degree_distribution, "degree-distribution.txt")
    return

if __name__ == "__main__": test()