boxes = []

with open('boxes.txt', 'r') as f:
    boxes = f.read().split('\n')

def slack(dimensions):
    smaller = 9999
    sides = calculateSideAreas(dimensions)
    for n in sides:
        if n < smaller:
            smaller = n
    return smaller

def calculateSideAreas(dimensions):
    l, w, h = dimensions
    sides = [l*w, w*h, h*l]
    return sides

def calculateArea(dimensions):
    l, w, h = dimensions
    return 2*l*w + 2*w*h +2*h*l

def calculateRibbonLength(dimensions):
    smallest = removeLargestSide(dimensions)
    return 2*smallest[0] + 2*smallest[1]

def calculateBowLength(dimensions):
    return dimensions[0] * dimensions[1] * dimensions[2]

def removeLargestSide(dimensions):
    largestIndex = -1 
    largest = -1
    for index, n in enumerate(dimensions):
        if n > largest:
            largest, largestIndex = n, index
    del dimensions[largestIndex]
    return dimensions

def calculateTotal():
    total = 0
    for box in boxes:
        if box == '':
            continue
        dimensions = box.split('x')
        dimensions = [int(dimensions[0]), int(dimensions[1]) ,int(dimensions[2])]
        total += calculateArea(dimensions) + slack(dimensions)
    return total

def calculateRibbon():
    total = 0
    for box in boxes:
        if box == '':
            continue
        dimensions = box.split('x')
        dimensions = [int(dimensions[0]), int(dimensions[1]) ,int(dimensions[2])]
        total += calculateBowLength(dimensions) + calculateRibbonLength(dimensions)
    return total

print(calculateTotal())
print(calculateRibbon())
