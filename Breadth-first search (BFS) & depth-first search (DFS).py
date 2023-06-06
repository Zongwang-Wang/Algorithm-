graph = {'s':['a','b'],
         'a':['c','s'],
         'b':['c','d','s'],
         'c':['a','b','d','e'],
         'd':['b','c','e'],
         'e':['c','d']
         }

def BFS(graph):
    que = []
    start_node = next(iter(graph))
    que.append((start_node, 0))  # Tuple of node and its distance from the start node
    checked = set()
    while que:
        current_node, distance = que.pop(0)
        if current_node not in checked:
            print(f"Node: {current_node}, Distance from start: {distance}")
            checked.add(current_node)
            for neighbor in graph[current_node]:  # Add neighbors of the current node to the queue
                que.append((neighbor, distance + 1))

BFS(graph)

def DFS(graph):
    stack = []
    start_node = next(iter(graph))
    stack.append(start_node)
    checked = set()

    while stack:
        current_node= stack.pop()
        if current_node not in checked:
            print(f"Node: {current_node}")
            checked.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in checked:
                    stack.append(neighbor)

DFS(graph)
