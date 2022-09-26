class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {'M':1000, 
                 'CM':900, 
                 'D':500, 
                 'CD':400, 
                 'C':100, 
                 'XC':90, 
                 'L':50, 
                 'XL':40,
                 'X':10, 
                 'IX':9,  
                 'V':5,
                 'IV':4,  
                 'I':1}
        
        s = ''
        
        for i,j in roman.items():
            
            if num // j == 0:
                pass
            else: 
                s = s + i * (num //j)
                num = num - (num // j)*j
        
        return s
        