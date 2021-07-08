class Solution(object):
    def permute(self, nums):
        ans = []
        
        self.helper(nums, [], ans)
        return ans
        
    def helper(self, nums, tmp, ans):
        if len(nums) == 0:
            ans.append(tmp)
            return
        
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], tmp + nums[i], ans)
        

        