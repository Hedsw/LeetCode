class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitlen = len(digits)
        newNum = 0
        
        for i in range(digitlen):
            newNum += 10**(digitlen-i-1)*digits[i]
        newNum += 1
        newstr = str(newNum)
        res = [] 
        for i in range(len(newstr)):
            res.append(int(newstr[i]))
        
        return res
        