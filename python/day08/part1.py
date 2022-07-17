import re
inputs = []

with open('input.txt', 'r') as f:
    inputs = f.read().split('\n')

# inputs = ['"\\\\"']
# print(inputs[0])
# print(len(inputs[0]))
# print(re.sub('\\\\\\\\', 'a', inputs[0]))
# print(len(re.sub('\\\\\\\\', 'a', inputs[0])))

total = 0
totalInMemory = 0
for st in inputs:
    if len(st) == 0:
        continue
    total += len(st)
    print(st, len(st))
    newSt = st
    if re.search('\\\\x', newSt):
        newSt = re.sub('\\\\x..', 'a', newSt)
    if re.search('\\\\"', newSt):
        newSt = re.sub('\\\\"', 'a', newSt)
    if re.search('\\\\\\\\', newSt):
        newSt = re.sub('\\\\\\\\', 'a', newSt)
    if re.search('\"', newSt):
        newSt = re.sub('\"', '', newSt)
    totalInMemory += len(newSt)
    print(newSt, len(newSt))


print(total - totalInMemory)
# print(inputs)

