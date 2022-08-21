class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(' ')
        output = []
        
        for word in s:
            output.append(''.join(reversed(word)))
        return ' '.join(output)