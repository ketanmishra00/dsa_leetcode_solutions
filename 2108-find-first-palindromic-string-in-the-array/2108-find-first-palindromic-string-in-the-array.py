class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        li=[]
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                li.append(words[i])
        if len(li)==0:
            return ""
        else:
            return li[0]
            