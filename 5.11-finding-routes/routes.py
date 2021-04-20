import collections
import csv
import json
import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines

def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports

def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = collections.defaultdict(set)
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            start = line[2]
            end = line[4]
            routes[start].add(end)
            routes[end].add(start)
    return routes

def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    visited = set([source])
    paths = []
    open_paths = [[source]]
    curr_segments=0
    while curr_segments <= max_segments and open_paths:
        curr_segments += 1
        new_open_paths = []
        for open_path in open_paths:
            for next_segment in routes[open_path[-1]] - visited:
                new_path = open_path + [next_segment]
                if next_segment == dest:
                    paths += [new_path]
                else:
                    new_open_paths += [new_path]
                    visited.add(next_segment)
        open_paths = new_open_paths
    return paths

def rename_path(path, airports):
    return tuple(map(airports.get, path))

def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = collections.defaultdict(list)
    for path in paths:
        output[len(path)-1].append(rename_path(path, airports))

    with open(f"{source}->{dest} (max {max_segments}).json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
