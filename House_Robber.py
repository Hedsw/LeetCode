



class Solution:
    def rob(self, nums: List[int]) -> int:
        evenList = nums[0:len(nums):2]
        oddList = nums[1:len(nums):2]
        
        print(sum(evenList))
        print(sum(oddList))
        
        maxEven = sum(evenList)
        maxOdd = sum(oddList)
        
        return max(maxEven, maxOdd)