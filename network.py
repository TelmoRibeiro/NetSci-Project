def get_filenames():
    from sys import argv as console_arguments
    if len(console_arguments) != 1 and len(console_arguments) != 4:
        raise Exception("number of arguments not expected")
    if len(console_arguments) == 1:
        meets_file = "meets.csv"
        phone_file = "phone.csv"
        roles_file = "roles.csv"
        return meets_file, phone_file, roles_file
    meets_file = console_arguments[1]
    phone_file = console_arguments[2]
    roles_file = console_arguments[3]
    return meets_file, phone_file, roles_file

def read_file(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def extract_edges(filename, roles_file=False):
    file_data = read_file(filename)
    file_data = file_data.splitlines()
    edges = []
    for edge in file_data:
        edge = edge.split(',')
        if roles_file and len(edge) < 4: 
            edge.append('')
        edges.append(edge)
    return edges[1:]

def build_network(filename, roles_file=False):
    edges = extract_edges(filename, roles_file)
    return edges

def print_network(network):
    for edge in network:
        print(edge)
    print()
    return

def main():
    meets_file, phone_file, roles_file = get_filenames()
    meets_network = build_network(meets_file)
    phone_network = build_network(phone_file)
    roles_network = build_network(roles_file, True)
    ''' TO DO '''
    print_network(meets_network)
    print_network(phone_network)
    print_network(roles_network)
    return

if __name__ == "__main__": main()

'''
RUN METHOD 1:
$ python proto.py
RUN METHOD 2:
$ python proto.py [meets_file] [phone_file] [roles_file]
'''