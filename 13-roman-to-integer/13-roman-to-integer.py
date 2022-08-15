class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValue = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        total = 0
        i = 0
        while i < len(s)-1:
            if s[i] + s[i + 1] in symbolToValue.keys():
                total += symbolToValue[s[i] + s[i + 1]]
                i += 2
            else:
                total += symbolToValue[s[i]]
                i += 1
        if i == len(s)-1:
            total += symbolToValue[s[-1]]
        return total