class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        arr, low, high = [0 for _ in range(len(s) + 1)], 0, len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                arr[i] = low
                low += 1
            else:
                arr[i] = high
                high -= 1
        arr[len(s)] = high
        return arr