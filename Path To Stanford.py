# This is the final project of 2023 Code in Place, which is a 6-week online course that covers the fundamentals of computer programming using the Python 
# programming language offered by Stanford university. Equivalent to CS106A
# My project is called path to Stanford that utilzied Dijkstra's shortest-path algorithm to find the shortest path from 8 major US cities to Stanford University

graph = {
    "Stanford University": {},
    "Los Angeles": {"Stanford University": 340},
    "Las Vegas": {"Stanford University": 390},
    "Chicago": {"Los Angeles": 1750},
    "Denver": {"Las Vegas": 620, "Los Angeles": 830},
    "New York City": {"Chicago": 790, "Columbus": 530},
    "Austin": {"Las Vegas": 1080, "Denver": 770},
    "Columbus": {"Austin": 1100, "Denver": 1150,"Chicago":275},
    "Miami": {"Austin": 1100, "New York City": 1100},
}

def select_start_city():
    cities = ["Los Angeles", "Las Vegas", "Chicago", "Denver", "New York City", "Austin", "Columbus", "Miami"]
    while True:
        print(
'Stanford University <--- Los Angeles <--- Chicago  <----+\n'
'     |         (340)        | (1750)      |             |\n'
'     ^                      ^             ^             ^\n'
'     |                      | (830)       | (275)       | (790)\n'
'     +<--- Las Vegas <--- Denver <--- Columbus <------ New York City\n'
'     (390)     |     (620)  | (1150)      | (530)       | (1100)\n'
'               ^            ^             v             ^\n'
'     (1080)    |            |             |             |\n'
'               +------------+--<-------Austin <------Miami\n'
'                                 (770)       (1100)\n')
        
        start_city = input("No matter where you start, you will always find your way to Stanford!!!\nPlease enter your starting city from the following options: " +
                           ", ".join(cities) + ": ")
        if start_city in cities:
            return start_city
        else:
            print("Invalid city. Please enter a valid city.")

def dijkstra(graph, start):
    distances = {city: float('infinity') for city in graph}
    distances[start] = 0
    queue = [start]
    previous_cities = {city: None for city in graph}

    while queue:
        current_city = min(queue, key=lambda city: distances[city])  # Get the city with the smallest distance
        queue.remove(current_city)

        for neighbour, distance in graph[current_city].items():
            new_distance = distances[current_city] + distance

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous_cities[neighbour] = current_city
                queue.append(neighbour)
    
    return distances, previous_cities

def shortest_path(graph, start, end):
    distances, previous_cities = dijkstra(graph, start)
    path = []
    while end is not None:
        path.append(end)
        end = previous_cities[end]
    path = path[::-1]
    return path, distances[path[-1]]

def main():
    start_city = select_start_city()
    path, distance = shortest_path(graph, start_city, "Stanford University")
    print("The shortest path from", start_city, "to Stanford University is:")
    print(" -> ".join(path))
    print("The total distance is:", distance, "miles.")
    print("I wish one day our dream will come ture! Good Luck!!!")
    print("p.s.: I used Dijkstra's shortest-path algorithm to make this work :)")

if __name__ == "__main__":
    main()
