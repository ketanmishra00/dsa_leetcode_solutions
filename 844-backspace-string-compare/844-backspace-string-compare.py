class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while "#" in s: s = re.sub(r'\w?#', '', s, count=1)
        while "#" in t: t = re.sub(r'\w?#', '', t, count=1)
        return s==t
        