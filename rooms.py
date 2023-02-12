"""
The function room_count() gets as an input a house represented
by n x m grid and outputs the count of rooms in the house.
The grid consists of two different characters:
    "."   denotes floor
    "#"   denotes wall
The algorithm works efficiently when 1 <= n, m <= 20.
The function neighbours() is a recursive help function.
"""

def room_count(blueprint):
    n = len(blueprint)
    m = len(blueprint[0])
    visited = [[False for i in range(m)] for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(m):
            if blueprint[i][j] == "." and not visited[i][j]:
                counter += 1
                neighbours(i, j, visited, blueprint)
    return counter
    
def neighbours(x, y, visited, blueprint):
    visited[x][y] = True
    adjacent = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    for i in range(4):
        x_ = adjacent[i][0]
        y_ = adjacent[i][1]
        if blueprint[x_][y_] == "." and not visited[x_][y_]:
            neighbours(x_, y_, visited, blueprint)

if __name__ == "__main__":
    blueprint = [
         "########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(room_count(blueprint)) # 3
