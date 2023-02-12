"""
This function calculates how many different squares of a 2D grid a robot visits given a motion cycle. 
The initial coordinate of the robot is (0,0).
Input: 
The motion cycle is given as a string consisting of following characters:
    "U" ---- Up
    "D" ---- Down
    "L" ---- Left
    "R" ---- Right
The algorithm is efficient up to 10^5 movements.
"""

def square_count(movements: str):
    x = 0
    y = 0
    coordinates = {0: [0]}
    result = 1

    for char in movements:
        if char in "UD":
            if char == "U":
                y += 1
            elif char == "D":
                y -= 1
            if y not in coordinates[x]:
                coordinates[x].append(y)
                result += 1
        else:
            if char == "L":
                x -= 1
            elif char == "R":
                x += 1
            if x not in coordinates:
                coordinates[x] = [y]
                result += 1
            elif x in coordinates and y not in coordinates[x]:
                coordinates[x].append(y)
                result += 1

    return result

print(square_count("LDLRLLRDL")) # 7
print(square_count("LL")) # 3
print(square_count("UUDLRR")) # 5
print(square_count("UDUDUDU")) # 2
