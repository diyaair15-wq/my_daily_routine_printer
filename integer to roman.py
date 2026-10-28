class RomanConverter:
    def __init__(self):
        self.mapping = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def to_roman(self, number):
        result = ""
        for value, symbol in self.mapping:
            count = number // value
            result += symbol * count
            number %= value
        return result


converter = RomanConverter()
print(converter.to_roman(2026))
