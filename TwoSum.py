class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [0,0]
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i != j and target - nums[i] == nums[j]:
                    return [i,j]