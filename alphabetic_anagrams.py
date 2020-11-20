from math import factorial


def listPosition(word: str):
    """Return the anagram list position of the word"""
    def perm(items, letter):
        pos = items.index(letter)
        return factorial(len(items) - 1) * pos

    result = 1
    sort_list = sorted(word)
    for i in range(len(word)):
        result += perm(sort_list, word[i])
        sort_list.pop(sort_list.index(word[i]))
    return result


print(listPosition('BOOKKEEPER'))
# testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4, 'QUESTION': 24572, 'BOOKKEEPER': 10743}
# testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4}

# for word in testValues:
#     assert listPosition(word) == testValues[word], 'Incorrect list position for: ' + word

# for word in testValues:
#     listPosition(word)
