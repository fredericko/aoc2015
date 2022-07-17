import re
inputs = []
named = {}
with open('input.txt', 'r') as f:
    inputs = f.read().split('\n')


for index, input in enumerate(inputs):
    inputs[index] = input.split('->')[::-1]
    name = inputs[index][0].replace(' ', '')
    if name != '':
        named[name] = inputs[index][1].strip()
          
inputs.clear()

def calculate(start, path):

    if start not in path:
        return start

    if 'RSHIFT' in path[start]:
        name = path[start].split('RSHIFT')[0].strip()
        value = path[start].split('RSHIFT')[1].strip()
        path[start] = str(int(calculate(name, path)) >> int(value))

    if 'LSHIFT' in path[start]:
        name = path[start].split('LSHIFT')[0].strip()
        value = path[start].split('LSHIFT')[1].strip()
        path[start] = str(int(calculate(name, path)) << int(value))

    if 'AND' in path[start]:
        name = path[start].split('AND')[0].strip()
        value = path[start].split('AND')[1].strip()
        path[start] = str(int(calculate(name, path)) & int(calculate(value, path)))

    if 'OR' in path[start]:
        name = path[start].split('OR')[0].strip()
        value = path[start].split('OR')[1].strip()
        path[start] = str(int(calculate(name, path)) | int(calculate(value, path)))

    if 'NOT' in path[start]:
        name = path[start].split('NOT')[1].strip()
        path[start] = ~ int(calculate(name, path))

    return path[start] if re.search('\d+$', str(path[start])) else calculate(path[start], path)

# print(inputs)
# assert calculate('d', named) == '72'
# assert calculate('e', named) == '507'
# assert calculate('f', named) == '492'
# assert calculate('g', named) == '114'
# assert calculate('h', named) == '65412'
# assert calculate('i', named) == '114'
# print(named)

named['b'] = '956'
print(calculate('a', named))

