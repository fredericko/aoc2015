with open('directions.txt', 'r') as f:
    directions = list(f.read())

floor = 0
firstTimeBasement = -1

for index, direction in enumerate(directions):
    if direction == "(":
        floor = floor + 1
    elif direction == ")":
        floor = floor - 1
    if floor == -1 and firstTimeBasement == -1:
        firstTimeBasement = index +1
    
print("Last Floor", floor, "First Time basement", firstTimeBasement)

