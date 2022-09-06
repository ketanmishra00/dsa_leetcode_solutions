class Solution:
    def rotateString(self, s: str, goal: str):
        l = set()
        i = len(goal)
        while i:
            i -= 1
            l.add(goal[i:] + goal[:i])
        return s in l