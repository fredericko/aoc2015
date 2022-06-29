vowels = ['a', 'e', 'i', 'o', 'u']
forbiddenWords = ['ab', 'cd', 'pq', 'xy']
words = []

with open('strings.txt', 'r') as f:
    words = f.read().split('\n')

def countVowels(word):
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    return count

def hasForbiddenString(word):
    for forbidden in forbiddenWords:
        if forbidden in word:
            return True
    return False

def hasDoubledString(word):
    i = chr
    for i in range(ord('a'), ord('z') + 1):
        if chr(i)*2 in word:
            return True
    return False

def isNaughty(word):
    return countVowels(word) < 3 or hasForbiddenString(word) or not hasDoubledString(word)


assert isNaughty('ugknbfddgicrmopn') == False
assert isNaughty('aaa') == False
assert isNaughty('jchzalrnumimnmhp') == True
assert isNaughty('haegwjzuvuyypxyu') == True
assert isNaughty('dvszwmarrgswjxmb') == True

def countNice(words):
    count = 0
    for word in words:
        if not isNaughty(word):
            count += 1
    return count

print(countNice(words))
