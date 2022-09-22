class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = list(s)
        n = len(string)
        reverse = True
        
        for i in range(0, n, k):
            if reverse:
                left = i
                right = min(i + k - 1, n - 1)

                while left < right:
                    string[left], string[right] = string[right], string[left]
                    left += 1
                    right -= 1
                    
            reverse = not reverse
            
        return ''.join(string)