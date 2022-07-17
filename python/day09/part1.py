inputs = []
paths = {}
with open('input.txt', 'r') as f:
    inputs = f.read().strip().split('\n')

for index, inp in enumerate(inputs):
    inputs[index] = inp.split(' = ')
    paths[inputs[index][0].split(' to ')[0]] = {'to': {}} 


for index, inp in enumerate(inputs):
    inputs[index][0] = inputs[index][0].split(' to ')
    paths[inputs[index][0][0]]['to'][inputs[index][0][1]] = inputs[index][1]


# [inputs[index][0][1], inputs[index][1]]
print(paths)
