class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitNum = 0
        for i in range(len(digits)):
            digitNum += (10**(len(digits)-i-1))*digits[i]
        digitNum += 1
        temp = []
        for i in str(digitNum):
            temp.append(int(i))
       
        return temp
     