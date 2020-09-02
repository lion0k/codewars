class RomanNumerals:
    roman = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    arab = {v: k for k, v in roman.items()}

    @classmethod
    def _get_arab_from_dic(cls, x):
        near = 0
        int_x = int(x)
        for key, val in cls.arab.items():
            if near <= key:
                near = key
            if key == int_x:
                return val
        if len(x) == 2:
            if 10 <= int_x < 40:
                return cls.arab[10] * int(x[:1])
            else:
                return cls.arab[50] + cls.arab[10] * (int(x[:1]) - 5)
        elif len(x) == 3:
            if 100 <= int_x < 400:
                return cls.arab[100] * int(x[:1])
            else:
                return cls.arab[500] + cls.arab[100] * (int(x[:1]) - 5)
        else:
            return cls.arab[1000] * int(x[:1])

    @classmethod
    def to_roman(cls, x):
        inp = str(x)[::-1]
        out = []
        for i in range(0, len(inp)):
            curr = inp[i] + '0' * i
            if inp[i] == '0':
                continue
            out.append(cls._get_arab_from_dic(curr))
        return ''.join(out[::-1])

    @classmethod
    def from_roman(cls, x):
        if not x:
            return 0
        out = []
        len_x = len(x)
        next_iter = False
        for i in range(len_x):
            if next_iter:
                next_iter = False
                continue
            if (x[i] == 'I' and i + 1 != len_x and x[i + 1] in ('V', 'X')) or\
               (x[i] == 'X' and i + 1 != len_x and x[i + 1] in ('L', 'C')) or \
               (x[i] == 'C' and i + 1 != len_x and x[i + 1] in ('D', 'M')):
                next_iter = True
                out.append(cls.roman[x[i] + x[i + 1]])
            else:
                out.append(cls.roman[x[i]])
        return sum(out)



print(RomanNumerals().from_roman('MCMXC'))

#
#
# assert RomanNumerals().to_roman(1000) == 'M', '1000 should == "M"'
# assert RomanNumerals().to_roman(1990) == 'MCMXC', '1990 should == "MCMXC"'
#
# assert RomanNumerals().to_roman('XXI') == 21, 'XXI should == 21'
# assert RomanNumerals().to_roman('MMVIII') == 2008, 'MMVIII should == 2008'
