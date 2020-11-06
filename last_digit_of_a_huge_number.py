from functools import reduce


def _last_digit(n1, n2):
    n1, n2 = n2, n1

    if (n1 == 0 and n2 == 0) or (n2 == 0):
        return 1

    if n1 < 10 and n2 < 10:
        return int(str(n1 ** n2))

    last_n1 = str(n1)[-1]
    last_n2 = str(n2)[-1]

    if (last_n1 == '1' and last_n2 == '1') or (last_n1 == '0' and last_n2 == '0'):
        return int(last_n1)

    last_n1 = str(n1)
    last_n1 = last_n1[len(last_n1) - 2:len(last_n1) + 1]
    last_n2 = str(n2)
    last_n2 = last_n2[len(last_n2) - 2:len(last_n2) + 1]
    if last_n2.startswith('0'):
        last_n2 = '{}{}'.format(1, last_n2)
    # print(last_n1, last_n1.startswith('0'))
    if last_n1.startswith('0'):
        last_n1 = '{}{}'.format(1, last_n1)

    # print('last1 - ', last_n1, 'last2 - ', last_n2)
    return int(str(int(last_n1) ** int(last_n2)))


def last_digit(lst):
    if not lst:
        return 1

    lst.reverse()
    return str(reduce(_last_digit, lst[1:], lst[0]))[-1]


test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6),
    ([2, 2, 101, 2], 6)
]

for data, res in test_data:
    print(last_digit(data), 'res ', res)

# print(_last_digit(123232, 92))
