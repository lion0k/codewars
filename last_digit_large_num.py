# Test.assert_equals(last_digit(4, 1), 4)
# Test.assert_equals(last_digit(4, 2), 6)
# Test.assert_equals(last_digit(9, 7), 9)
# Test.assert_equals(last_digit(10, 10 ** 10), 0)
# Test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
# Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)


def last_digit(n1, n2):
    if (n1 == 0 and n2 == 0) or (n2 == 0):
        return 1

    if n1 < 10 and n2 < 10:
        return int(str(n1 ** n2)[-1])

    last_n1 = str(n1)[-1]
    last_n2 = str(n2)[-1]

    if last_n1 == '1' and last_n2 == '1':
        return int(last_n1)
    if last_n1 == '0' and last_n2 == '0':
        return int(last_n1)

    last_n1 = str(n1)
    last_n1 = last_n1[len(last_n1) - 2:len(last_n1) + 1]
    last_n2 = str(n2)
    last_n2 = last_n2[len(last_n2) - 2:len(last_n2) + 1]

    return int(str(int(last_n1) ** int(last_n2))[-1])
