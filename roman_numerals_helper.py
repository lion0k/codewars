class RomanNumerals:
    info = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    def _get_roman_from_dic(self, x):
        if x == '0':
            return ''
        for key, val in self.info.items():
            if val == int(x):
                return key
        return ''

    def to_roman(self, x):
        inp = str(x)[::-1]
        out = []
        for i in range(0, len(inp)):
            out.append(inp[i] + '0' * i)
        return out




    def from_roman(self, x):
        pass


print(RomanNumerals().to_roman(1990))

#
#
# assert RomanNumerals().to_roman(1000) == 'M', '1000 should == "M"'
# assert RomanNumerals().to_roman(1990) == 'MCMXC', '1990 should == "MCMXC"'
#
# assert RomanNumerals().to_roman('XXI') == 21, 'XXI should == 21'
# assert RomanNumerals().to_roman('MMVIII') == 2008, 'MMVIII should == 2008'
