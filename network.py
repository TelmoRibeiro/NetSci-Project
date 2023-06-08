def load_files():
    from sys import argv as console_arguments
    if len(console_arguments) != 1 and len(console_arguments) != 6:
        raise Exception("number of arguments not expected")
    if len(console_arguments) == 1:
        connc_file = "connc.csv"
        meets_file = "meets.csv"
        phone_file = "phone.csv"
        roles_file = "roles.csv"
        stats_file = "stats.csv"
        return connc_file, meets_file, phone_file, roles_file, stats_file
    connc_file = console_arguments[1]
    meets_file = console_arguments[2]
    phone_file = console_arguments[3]
    roles_file = console_arguments[4]
    stats_file = console_arguments[5]
    return connc_file, meets_file, phone_file, roles_file, stats_file

def read_file(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def extract_edges(filename):
    file_data = read_file(filename)
    file_data = file_data.splitlines()
    edges = []
    for edge in file_data:
        edge = edge.split(',')
        edges.append(edge)
    return edges[1:]

def build_network(filename):
    edges = extract_edges(filename)
    return edges

def print_network(network):
    for edge in network:
        print(edge)
    print()
    return

def main():
    connc_file, meets_file, phone_file, roles_file, stats_file = load_files()
    connc_network = build_network(connc_file)
    meets_network = build_network(meets_file)
    phone_network = build_network(phone_file)
    # roles_file is an attribute file
    # stats_file is an attribute file 
    ''' TO DO '''
    print_network(connc_network)
    print_network(meets_network)
    print_network(phone_network)
    return

if __name__ == "__main__": main()

'''
RUN METHOD 1:
$ python network.py
RUN METHOD 2:
$ python network.py [connc_file ][meets_file] [phone_file] [roles_file] [stats_file]
'''