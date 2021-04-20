from dictionaries import neighbours_dictionary, heuristic_disctionary

start_node = 'Arad'
goal_node = "Bucharest"


def greedy_bfs():
    visited_nodes = [start_node]
    while True:
        current_node = visited_nodes[-1]
        neighbours = neighbours_dictionary[current_node]
        next_node = select_best_neighbour(neighbours, visited_nodes)
        if next_node == goal_node:
            print('GOAL NODE FOUND')
            visited_nodes.append(next_node)
            break
        elif next_node == -1:
            print('GOAL NODE NOT FOUND')
            break
        visited_nodes.append(next_node)

    print(visited_nodes)


# for positive heuristic values only
def select_best_neighbour(neighbours, visited_nodes):
    min_heuristic = heuristic_disctionary[goal_node][start_node]
    possible_next_node = -1
    for city in neighbours:
        if city in visited_nodes:
            pass
        elif heuristic_disctionary[goal_node][city] < min_heuristic:
            min_heuristic = heuristic_disctionary[goal_node][city]
            possible_next_node = city

    return possible_next_node

