from collections import Counter

def play(cards):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def is_royal_flush(items: list) -> bool:
        return ''.join(items) == '10JQKA'

    def is_numerical_order(items: list) -> bool:
        first = order.index(items[0])
        if first == 9:
            return False
        return order[first:first + 5] == items

    def is_four_of_kind(items: dict) -> bool:
        return 4 in items.values()

    def is_full_house(items: dict) -> bool:
        return (len(items) == 2) and (3 in items.values())

    def is_three_of_kind(items: dict) -> bool:
        return 3 in items.values()

    def is_two_pairs(items: dict) -> bool:
        return (len(items) == 3) and (2 in items.values())

    def is_pair(items: dict) -> bool:
        return 2 in items.values()

    x = cards.split()
    num = [i[:-1] for i in x]
    num.sort(key=lambda v: order.index(v))
    num_c = Counter(num)
    suit = set(i[-1] for i in x)

    if len(suit) == 1:
        if is_royal_flush(num):
            # print('Royal Flush')
            return 'Royal Flush'
        elif is_numerical_order(num):
            # print('Straight Flush')
            return 'Straight Flush'
        else:
            # print('Flush')
            return 'Flush'
    else:
        if is_four_of_kind(num_c):
            # print('Four of a Kind')
            return 'Four of a Kind'
        elif is_full_house(num_c):
            # print('Full House')
            return 'Full House'
        elif is_numerical_order(num):
            # print('Straight')
            return 'Straight'
        elif is_three_of_kind(num_c):
            # print('Three of a Kind')
            return 'Three of a Kind'
        elif is_two_pairs(num_c):
            # print('Two Pairs')
            return 'Two Pairs'
        elif is_pair(num_c):
            # print('Pair')
            return 'Pair'
        # print('High Card')
        return 'High Card'


tests = {'10C JC QC KC AC': 'Royal Flush',
         '5D 10H AS 5C AD': 'Two Pairs',
         '2D 8H AS KS JS': 'High Card',
         'AH 3C 5C JS 5H': 'Pair',
         '5D 5H 3C 5S 9C': 'Three of a Kind',
         '5S 3H 6C 7C 4S': 'Straight',
         'AS JS 9S 2S QS': 'Flush',
         '7H 7D AC AH AS': 'Full House',
         '8S 8C 5C 8D 8H': 'Four of a Kind',
         'QD JC 10S 9H KS': 'Straight',
         'QH JH AH KH 10H': 'Royal Flush',
         '9H KH QH 10H JH': 'Straight Flush',
         '2S QS 6D AS 5D': 'High Card',
         '3H QH 10C 6C 6H': 'Pair',
         '3D 6C QC 3H AS': 'Pair',
         '7H 9H 6S 9C 6H': 'Two Pairs',
         'QS 3H KS 2S QH': 'Pair',
         '10S 10C 8D 3S 6D': 'Pair',
         '6S 9H 4S 2D 5D': 'High Card',
         'QD 6H 7D 8S 7S': 'Pair',
         '6D 9H QH AD KD': 'High Card',
         '5C JC 3S 10H 5H': 'Pair',
         '7S 9H AD KS 3D': 'High Card',
         '2H 6H 7H AD 6C': 'Pair',
         '8D QD 10C 2S 7S': 'High Card',
         'JC KH 10S QH KD': 'Pair',
         '9S 7S 9C QC 10S': 'Pair',
         'QD 8D JH 2H 10C': 'High Card',
         '10S 4D 3S QD AS': 'High Card',
         '4S 7C 7H 4H JS': 'Two Pairs',
         '9D 6D 2C 2H JS': 'Pair',
         'QC QD 2D 9H 7C': 'Pair',
         'KH JC 9D KS 4C': 'Pair',
         '7C 3D 3S 8H KD': 'Pair',
         'AS 10S 2C 2H 7D': 'Pair',
         'KH 2H 4C KS 3C': 'Pair',
         '2D QH KC 7S 10S': 'High Card',
         '3C AD QH AH 5C': 'Pair',
         '8C JC JH AC 10S': 'Pair',
         '2C QC 6C JD 8C': 'High Card',
         '3D 10D AS 10C 7D': 'Pair',
         '3D 3S 5S 8S JH': 'Pair',
         'JS 4H 8C 2C 7S': 'High Card',
         '3H JH 7C 4D 7S': 'Pair',
         '8D 10S AH 7C 8C': 'Pair',
         'JS 3H 5C 4H 8C': 'High Card',
         '6C 2S 6S 8S KC': 'Pair',
         '7S 8C 5C 10D 3S': 'High Card',
         '10D 9H JC KS 3C': 'High Card',
         '4H 8C AC 7D QD': 'High Card'}

for k, v in tests.items():
    assert play(k) == v, play(k) + ' ' + k
