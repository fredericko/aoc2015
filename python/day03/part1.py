directions = open('directions.txt', 'r')

directions =  list(directions.read().replace('\n', ''))
x=0
y=0
positions = []

for direction in directions:
    if direction == '>':
        x += 1
    if direction == '^':
        y += 1
    if direction == '<':
        x -= 1
    if direction == 'v':
        y -= 1
    positions.append(str(x)+str(y))

total = list(dict.fromkeys(positions))
print(len(total))
