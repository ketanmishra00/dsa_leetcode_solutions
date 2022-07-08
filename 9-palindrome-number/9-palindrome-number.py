class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        if x<0:
            return False
        while ( temp != 0):
            rem = temp% 10
            rev = rev*10 + rem
            temp = temp // 10
        if (x==rev):
            return True
        else:
            return False