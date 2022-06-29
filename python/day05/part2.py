words = []

with open('strings.txt', 'r') as f:
    words = f.read().split('\n')

def countPairs(word):
    count = 0
    letters = list(word)
    size = len(letters)
    for index, letter in enumerate(letters):
        if size > index + 1 and word.count(letter+letters[index + 1]) > 1:
            count += 1
    return count

def repeatLetterOneSpaced(word):
    letters = list(word)
    size = len(letters)
    for index, letter in enumerate(letters):
        if size > index + 2 and letter == letters[index + 2]:
            return True
    return False

def isNice(word):
    return countPairs(word) > 0 and repeatLetterOneSpaced(word)


assert isNice('qjhvhtzxzqqjkmpb') == True
assert isNice('xxyxx') == True
assert isNice('uurcxstgmygtbstg') == False
assert isNice('ieodomkazucvgmuy') == False

def countNice(words):
    count = 0
    for word in words:
        if isNice(word):
            count += 1
    return count

print(countNice(words))
