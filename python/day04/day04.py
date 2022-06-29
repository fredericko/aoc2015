import hashlib

def findHash(secret, zeros):
    num = 1
    result = hashlib.md5(secret.encode('utf-8')+str(num).encode('utf-8'))
    while not result.hexdigest().startswith('0'*zeros, 0):
        num += 1
        result = hashlib.md5(secret.encode('utf-8')+str(num).encode('utf-8'))
    return num


assert findHash('abcdef', 5) == 609043
assert findHash('pqrstuv', 5) == 1048970


secret = 'ckczppom'
# Part1
print(findHash(secret, 5))

# Part2
print(findHash(secret, 6))
