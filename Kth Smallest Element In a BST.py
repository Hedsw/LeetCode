class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.helper(root, res)
        res = sorted(res)
        print(res)
        return res[k-1]

        
    def helper(self, root, res):            
        if root is None:
            return
        
        res.append(root.val)
        
        self.helper(root.left, res)
        self.helper(root.right, res)
        
        
                