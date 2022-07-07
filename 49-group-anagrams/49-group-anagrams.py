class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for x in strs:
            sort = str(sorted(x))
            if sort in anagram:
                anagram[sort].append(x)
            else:
                anagram[sort] = [x]
        return [x for _, x in anagram.items()]