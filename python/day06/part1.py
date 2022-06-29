instructions = []
grid =  [[False for i in range(1000)] for j in range(1000)]

with open('grid.txt', 'r') as f:
    instructions = f.read().split('\n') 

def turnOn(grid, instr):
    start = instr[0].split(',')
    end = instr[1].split(',')
    movx = int(end[0]) - int(start[0])
    movy = int(end[1]) - int(start[1])
    for x in range(movx + 1):
        for y in range(movy + 1):
            grid[int(start[0]) + x][int(start[1]) + y] = True
    return grid

def turnOff(grid, instr):
    start = instr[0].split(',')
    end = instr[1].split(',')
    movx = int(end[0]) - int(start[0])
    movy = int(end[1]) - int(start[1])
    for x in range(movx + 1):
        for y in range(movy + 1):
            grid[int(start[0]) + x][int(start[1]) + y] = False
    return grid

def toggle(grid, instr):
    start = instr[0].split(',')
    end = instr[1].split(',')
    movx = int(end[0]) - int(start[0])
    movy = int(end[1]) - int(start[1])
    for x in range(movx + 1):
        for y in range(movy + 1):
            grid[int(start[0]) + x][int(start[1]) + y] = not grid[int(start[0]) + x][int(start[1]) + y]
    return grid

def countOnLights(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                count += 1
    return count

def setupLights(grid, intructions):
    for instruction in instructions:
        if 'turn on' in instruction:
            grid = turnOn(grid, instruction.replace('turn on', '').replace(' ', '').split('through'))
        if 'turn off' in instruction:
            grid = turnOff(grid, instruction.replace('turn off', '').replace(' ', '').split('through'))
        if 'toggle' in instruction:
            grid = toggle(grid, instruction.replace('toggle', '').replace(' ', '').split('through'))
    return grid

#print(countOnLights(turnOn([[False, False], [False, False]], ['1,0', '1,1'])))
print(countOnLights(setupLights(grid, instructions)))
