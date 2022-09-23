class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        char = ''
        for i in range(0,min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                char = char + strs[0][i]
            else:
                break
        return char