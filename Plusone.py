class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitLen = len(digits)
        newNum = 0
        for i in range(digitLen):
            newNum += (10**(digitLen-i-1)) * digits[i]
        newNum += 1
        newStr = str(newNum)
        temp = []
        for i in newStr:
            temp.append(int(i))
        return temp