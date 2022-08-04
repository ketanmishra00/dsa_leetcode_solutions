class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        curr=0
        for i in range(len(sentences)):
            curr=len(sentences[i].split())
            if curr>maximum:
                maximum=curr
        return maximum
                              