class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        x = 1
        while x<=2**31 -1:
            if x == n:
                return True
            x*=2
        return False