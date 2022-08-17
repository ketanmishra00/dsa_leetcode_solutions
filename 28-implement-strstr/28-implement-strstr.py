class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        length = len(needle)
        l = 0 
        r = length - 1
        while r < len(haystack):
            if haystack[l:r+1] == needle:
                return l
            else:
                l += 1
                r += 1
        return -1