"""
2022/10/31

@see https://leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Create a dictionary to store the roman numerals
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # 2. Create a variable to store the total
        # 3. Convert string to list
        total = 0
        s = list(s)

        # 4. Loop through the string
        for i in range(len(s)):
            # 5. If the current roman numeral is less than the next roman numeral...
            if roman_numerals[s[i]] > roman_numerals[s[i - 1]] and i > 0:
                # 6. Subtract previous input and add the difference
                total -= roman_numerals[s[i - 1]]
                total += (roman_numerals[s[i]] - roman_numerals[s[i - 1]])
            else:
                # 7. Otherwise, add the current roman numeral to the total
                total += roman_numerals[s[i]]

        # 8. Return the total    
        return total        