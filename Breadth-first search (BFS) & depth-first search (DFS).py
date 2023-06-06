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

# the basic DFS search using a stack 
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

# Using the recursive approach to performe the topological search in a directed acyclic graph
graph2 = {'s':['v','w'],
         'v':['x'],
         'w':['x'],
         'x':[],
         }
visited = set() #place the global variable outside the recursive DFS function 
current_label = len(graph2)-1

def DFS(graph,start):
    global current_label
    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            DFS(graph,i)
            print(f"Node:{i}, Current Label: {current_label}")
            current_label -= 1
    if current_label == 0: 
        print((f"Node:{start}, Current Label: 0")) # Print the starting node with a current label of 0

DFS(graph2,'s')
