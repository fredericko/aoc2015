directions = open('directions.txt', 'r')

directions =  list(directions.read().replace('\n', ''))

santa1 = [0,0]
santa2 = [0,0]

positions = []
positions.append('0x0')

def move(santa, direction):
    if direction == '>':
        santa[0] += 1
    if direction == '^':
        santa[1] += 1
    if direction == '<':
        santa[0] -= 1
    if direction == 'v':
        santa[1] -= 1

def unique_deliveries(directions):
    for index, direction in enumerate(directions):
        if index % 2 == 0:
            move(santa1, direction)
            positions.append(str(santa1[0])+'x'+str(santa1[1]))
        else:
            move(santa2, direction)
            positions.append(str(santa2[0])+'x'+str(santa2[1]))

    total = list(dict.fromkeys(positions))
    return len(total)

# assert unique_deliveries(list('^v')) == 3
# assert unique_deliveries(list('^>v<')) == 3
# assert unique_deliveries(list('^v^v^v^v^v')) == 11

print(unique_deliveries(directions))
