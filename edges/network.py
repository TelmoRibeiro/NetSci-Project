def load_files():
    from sys import argv as console_arguments
    if len(console_arguments) != 1 and len(console_arguments) != 5:
        raise Exception("number of arguments not expected")
    if len(console_arguments) == 1:
        contacts_file   = "contacts.csv"
        meetings_file   = "meetings.csv"
        phonecalls_file = "phone_calls.csv"
        relations_file  = "relationships.csv" 
        return contacts_file, meetings_file, phonecalls_file, relations_file
    contacts_file   = console_arguments[1]
    meetings_file   = console_arguments[2]
    phonecalls_file = console_arguments[3]
    relations_file  = console_arguments[4]
    return contacts_file, meetings_file, phonecalls_file, relations_file

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

def merge_networks(networks):
    merged_network = []
    for network in networks:
        merged_network += network
    return merged_network

def print_network(network, filename=None):
    network_file = open(filename, 'w')
    print("network:\n")
    print("source,target,weight")
    network_file.write("source,target,weight\n")
    for edge in network:
        print(f"{edge[0]},{edge[1]},{edge[2]}")
        network_file.write(f"{edge[0]},{edge[1]},{edge[2]}\n")
    print()
    return

def main():
    contacts_file, meetings_file, phonecalls_file, relations_file = load_files()
    contacts_network   = build_network(contacts_file)
    meetings_network   = build_network(meetings_file)
    phonecalls_network = build_network(phonecalls_file)
    relations_network  = build_network(relations_file)
    final_network = merge_networks([contacts_network, meetings_network, phonecalls_network, relations_network])
    print_network(final_network, "network.csv")
    return

if __name__ == "__main__": main()

'''
RUN METHOD 1:
$ python network.py
RUN METHOD 2:
$ python network.py [connc_file ][meets_file] [phone_file] [roles_file] [stats_file]
'''