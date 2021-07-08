class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 0:
            return ans
        
        self.helper(nums, [], ans)
        #print(ans)
        return ans
        
    def helper(self, nums, tmp, ans):
        #if len(nums) == 0:
        ans.append(tmp) # 여기서 맨 처음에 []가 들어가기 때문에 위에서 append를 안해줘도 된다.
        for i in range(len(nums)):
            self.helper(nums[i+1:], tmp + [nums[i]], ans)
            #self.dfs(nums[i+1:], path+[nums[i]], ret)
       
            
