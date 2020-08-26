
def sum_pairs(ints, s):
    if not ints:
        return None

    x = set()
    for i in ints:
        y = s - i
        return [y, i] if i in x else x.add(y)
    return None


l1 = ([1, 4, 8, 7, 3, 15], 8)
l2 = ([1, -2, 3, 0, -6, 1], -6)
l3 = ([20, -13, 40], -7)
l4 = ([1, 2, 3, 4, 1, 0], 2)
l5 = ([10, 5, 2, 3, 7, 5], 10)
l6 = ([4, -2, 3, 3, 4], 8)
l7 = ([0, 2, 0], 0)
l8 = ([5, 9, 13, -3], 10)

for i in l1,l2,l3,l4,l5,l6,l7,l8:
    print(sum_pairs(*i))
