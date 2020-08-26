"""
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point

# Example
#  Throw       Score
# ---------   ------------------
# 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
# 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
# 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
"""


def score(dice):
    if not dice:
        return 0

    d_mult = [i*1000 if i == 1 else i*100 for i in range(1, 7)]
    conv = [str(i) for i in dice]
    s = ''.join(conv)

    out = 0
    ost = ''
    for i in range(1, 7):
        if s.count(str(i)) > 2:
            out += d_mult[i - 1]
            ost = s.replace(str(i), '', 3)
            break

    if ost:
        for j in ost:
            if j == '1':
                out += 100
            elif j == '5':
                out += 50
    else:
        for j in s:
            if j == '1':
                out += 100
            elif j == '5':
                out += 50
    return out
