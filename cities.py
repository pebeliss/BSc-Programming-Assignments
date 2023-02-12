"""
This code implements a class Cities.
The object of this class takes a number of cities (at most 50) as its input.
The class has two visible methods:
    .add_road(a, b)     adds a road between cities a and b
    .has_route(a, b)    checks does there exist a route between cities a and b
"""

class Cities:
    def __init__(self, n):
        self.cities = [[] for i in range(n+1)]
        self.visited = [False for i in range(n+1)]

    def add_road(self, a, b):
        self.cities[a].append(b)
        self.cities[b].append(a)

    def has_route(self, a, b):
        self.visited = [False for i in range(len(self.cities))]
        self.__visit(a)
        return self.visited[b]

    def __visit(self, a):
        self.visited[a] = True
        for neighbour in self.cities[a]:
            if not self.visited[neighbour]:
                self.__visit(neighbour)


if __name__ == "__main__":
    c = Cities(5)
    c.add_road(4,5)
    c.add_road(1,2)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True
    
