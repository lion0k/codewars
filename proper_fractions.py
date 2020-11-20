import unittest as ut

from math import ceil, sqrt


def get_all_dividers(num):

    first_half_dividers = [x for x in range(1, ceil(sqrt(num)) + 1)
                           if num % x == 0]

    second_half_dividers = [int(num / x) for x in reversed(first_half_dividers)
                            if int(num / x) not in first_half_dividers]

    return first_half_dividers + second_half_dividers


class Test_rr(ut.TestCase):


    def proper_fractions(self, n):
        res = 0
        for i in range(1, n):
            if self.gcd(i, n) == 1:
                res += 1

        return res

    def test_rete(self):
        self.assertEquals(self.proper_fractions(1), 0)
        self.assertEquals(self.proper_fractions(2), 1)
        self.assertEquals(self.proper_fractions(5), 4)
        self.assertEquals(self.proper_fractions(15), 8)
        self.assertEquals(self.proper_fractions(25), 20)

# proper_fractions(1)

# ut.main()

# x = Test_rr()
print(get_all_dividers(9898491512))