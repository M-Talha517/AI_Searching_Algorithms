path_cost_dictionary = \
    {
        "Oradea": {
            "Zerind": 71,
            "Sibiu": 151
        },
        "Zerind": {
            "Oradea": 71,
            "Arad": 75
        },
        "Arad": {
            "Zerind": 75,
            "Sibiu": 140,
            "Timisoara": 118
        },
        "Sibiu": {
            "Oradea": 151,
            "Arad": 140,
            "Fagaras": 99,
            "Rimnicu Vilcea": 80
        },
        "Timisoara": {
            "Arad": 118,
            "Lugoj": 111
        },
        "Lugoj": {
            "Timisoara": 111,
            "Mehadia": 70
        },
        "Mehadia": {
            "Lugoj": 70,
            "Dobreta": 75
        },
        "Dobreta": {
            "Mehadia": 75,
            "Craiova": 120
        },
        "Craiova": {
            "Dobreta": 120,
            "Rimnicu Vilcea": 146,
            "Pitesti": 138
        },
        "Rimnicu Vilcea": {
            "Sibiu": 80,
            "Craiova": 146,
            "Pitesti": 97
        },
        "Pitesti": {
            "Rimnicu Vilcea": 97,
            "Craiova": 138,
            "Bucharest": 101
        },
        "Bucharest": {
            "Pitesti": 101,
            "Giurgiu": 90,
            "Fagaras": 211,
            "Urziceni": 85
        },
        "Fagaras": {
            "Bucharest": 211,
            "Sibiu": 99
        },
        "Urziceni": {
            "Bucharest": 85,
            "Vaslui": 142,
            "Hirsova": 98
        },
        "Vaslui": {
            "Urziceni": 142,
            "Lasi": 92
        },
        "Lasi": {
            "Vaslui": 92,
            "Neamt": 87
        },
        "Neamt": {
            "Lasi": 87
        },
        "Giurgiu": {
            "Bucharest": 90
        },
        "Hirsova": {
            "Urziceni": 98,
            "Eforie": 86
        },
        "Eforie": {
            "Hirsova": 86
        }

    }

neighbours_dictionary = {

    "Oradea": ["Zerind", "Sibiu"],
    "Zerind": ["Oradea", "Arad"],
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Sibiu": ["Oradea", "Arad", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Dobreta"],
    "Dobreta": ["Mehadia", "Craiova"],
    "Craiova": ["Dobreta", "Rimnicu Vilcea", "Craiova"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Pitesti", "Giurgiu", "Fagaras", "Urziceni"],
    "Fagaras": ["Bucharest", "Sibiu"],
    "Urziceni": ["Bucharest", "Vaslui", "Hirsova"],
    "Vaslui": ["Urziceni", "Lasi"],
    "Lasi": ["Vaslui", "Neamt"],
    "Neamt": ["Lasi"],
    "Giurgiu": ["Bucharest"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"]

}

heuristic_disctionary = {
    "Bucharest":
        {
            "Arad": 366,
            "Bucharest": 0,
            "Craiova": 160,
            "Dobreta": 242,
            "Eforie": 161,
            "Fagaras": 178,
            "Giurgiu": 77,
            "Hirsova": 151,
            "Lasi": 226,
            "Lugoj": 244,
            "Mehadia": 241,
            "Neamt": 234,
            "Oradea": 380,
            "Pitesti": 10,
            "Rimnicu Vilcea": 193,
            "Sibiu": 253,
            "Timisoara": 329,
            "Urziceni": 80,
            "Vaslui": 199,
            "Zerind": 374
        }

}
