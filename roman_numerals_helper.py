class RomanNumerals:
    roman = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    arab = {v: k for k, v in roman.items()}

    def _get_arab_from_dic(self, x):
        print(x)
        near = 0
        int_x = int(x)
        for key, val in self.arab.items():
            if near <= key:
                near = key
            if key == int_x:
                return val
        if len(x) == 2:
            if 10 <= int_x < 40:
                return self.arab[10] * int(x[:1])
            else:
                return self.arab[50] + self.arab[10] * (int(x[:1]) - 5)
        elif len(x) == 3:
            if 100 <= int_x < 400:
                return self.arab[100] * int(x[:1])
            else:
                return self.arab[500] + self.arab[100] * (int(x[:1]) - 5)
        else:
            return self.arab[1000] * int(x[3:])

    def to_roman(self, x):
        inp = str(x)[::-1]
        out = []
        for i in range(0, len(inp)):
            curr = inp[i] + '0' * i
            if i == 0 and inp[i] == '0':
                continue
            elif inp[i] == '0':
                curr = '1' + curr
            out.append(self._get_arab_from_dic(curr))
        return ''.join(out[::-1])




    def from_roman(self, x):
        pass


print(RomanNumerals().to_roman(2008))

#
#
# assert RomanNumerals().to_roman(1000) == 'M', '1000 should == "M"'
# assert RomanNumerals().to_roman(1990) == 'MCMXC', '1990 should == "MCMXC"'
#
# assert RomanNumerals().to_roman('XXI') == 21, 'XXI should == 21'
# assert RomanNumerals().to_roman('MMVIII') == 2008, 'MMVIII should == 2008'
