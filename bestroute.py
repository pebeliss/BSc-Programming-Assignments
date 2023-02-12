"""
This code implements a class BestRoute.
The object constructor gets a number of cities (at most 50) as its input.
The class has two methods:
    .add_road(a, b, x)      adds a road with length x between cities a and b
    .find_route(a, b)       finds and return a shortest route between cities a and b
There can be at most 100 routes between cities with integer length 1 <= x <= 1000
The .find_route() method returns -1 if no route is found.

The class Edge implements edge objects representing direct routes between two cities,
as the city entity is modelled as an undirected graph.
"""

from heapq import heappush, heappop

class Edge:
    def __init__(self, end, length):
        self.end = end
        self.length = length

class BestRoute:
    def __init__(self, n):
        self.n = n
        self.cities = [[] for i in range(self.n+1)]

    def add_road(self, a, b, x):
        edge_a = Edge(b, x)
        edge_b = Edge(a, x)
        self.cities[a].append(edge_a)
        self.cities[b].append(edge_b)

    def find_route(self, a, b):
        distance = [(1000*50+1) for i in range(self.n+1)]
        visited = [False for i in range(self.n+1)]
        distance[a] = 0
        heap = []
        heappush(heap, (0, a))
        while len(heap) > 0:
            shortest = heappop(heap)
            u = shortest[1]
            if not visited[u]:
                visited[u] = True
                for edge in self.cities[u]:
                    v = edge.end
                    if distance[v] > distance[u] + edge.length:
                        distance[v] = distance[u] + edge.length
                        heappush(heap, (distance[v], v))
        if distance[b] == 1000*50+1:
            return -1
        else:
            return distance[b]

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3
