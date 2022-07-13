class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for char in s:
            if char.isupper():
                lst.append(char.lower())
            elif char.islower():
                lst.append(char)
            elif char.isdigit():
                lst.append(char)
        temp = lst[::-1]       
        return lst == temp

        