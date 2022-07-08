class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        t=s.split()
        return len(t[0])