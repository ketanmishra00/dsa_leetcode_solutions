class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        l = s.split()
        if len(l) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = l[i]
        return True
        