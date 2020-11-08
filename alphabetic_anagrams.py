import itertools as it


def listPosition(word):
    """Return the anagram list position of the word"""
    res = dict(zip(sorted(set(it.permutations(word))), it.count(1, 1)))
    return res[tuple(word)]


testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4, 'QUESTION': 24572, 'BOOKKEEPER': 10743}
# testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4}

for word in testValues:
    assert listPosition(word) == testValues[word], 'Incorrect list position for: ' + word

# for word in testValues:
#     listPosition(word)
