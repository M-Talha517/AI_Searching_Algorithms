from dictionaries import neighbours_dictionary, heuristic_disctionary, path_cost_dictionary

start_node = 'Arad'
goal_node = "Bucharest"


def a_star():
    # initialize priority queue with start_node in it
    priority_queue = PriorityQueue()
    goal_found = False
    # list of all visited nodes
    visited_nodes = []

    while priority_queue or not goal_found:
        current_node = priority_queue[0]
        visited_nodes.append(current_node)
        if current_node.city == goal_node:
            break
        priority_queue.remove(current_node)

        neighbours = neighbours_dictionary[current_node.city]
        # check if the node is an end node i.e. All neighbours are visited or no neighbour
        for neighbour in neighbours:
            # convert dictionary data to string for generic purpose
            neighbour = str(neighbour)
            if neighbour not in visited_nodes:
                # total path travelled from start node to current node + current node to neighbour node
                neighbour_GofN = current_node.GofN + int(path_cost_dictionary[current_node.city][neighbour])
                neighbour_node = Node(city=neighbour, GofN=neighbour_GofN, parent=current_node.city)
                priority_queue.priority_insert(neighbour_node)

    if priority_queue:
        print('GOAL NODE FOUND')
        print("VISITED NODES")
        for x in visited_nodes:
            print(x.city, end=' ')

        # calculating optimal path from visited nodes
        print("OPTIMAL PATH")
        optimal_path = [start_node]
        parent = start_node
        for child_node in visited_nodes:
            if child_node.parent == parent:
                optimal_path.append(child_node.city)
                parent = child_node.city
        print(optimal_path)


    else:
        print("goal node not found")


class PriorityQueue(list):
    def __init__(self):
        first_node = node = Node(city=start_node, GofN=0, parent='NO PARENT')
        self.priority_insert(first_node)

    def priority_insert(self, node):
        i = 0
        for i in range(0, len(self)):
            if self[i].FofN > node.FofN:
                break
        self.insert(i, node)


class Node:
    def __init__(self, city, parent, GofN):
        # name of node
        self.city = city
        # name of parent node
        self.parent = parent
        #  G(N) Path Cost Covered From Start Node to Current Node
        self.GofN = GofN
        #  H(N) Heuristic Cost from Goal Node
        self.HofN = int(heuristic_disctionary[goal_node][self.city])
        #  F(N) = G(N) + H(N)
        self.FofN = self.GofN + self.HofN
