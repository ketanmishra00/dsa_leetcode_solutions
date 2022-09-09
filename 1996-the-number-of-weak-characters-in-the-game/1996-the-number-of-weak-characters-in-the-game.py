class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key = lambda x: (-x[0],x[1]))
        maxdef = properties[0][1]
        count = 0
        for i in range(1,len(properties)):
            if properties[i][1] < maxdef:
                count +=1
            else:
                maxdef = properties[i][1]
        return count