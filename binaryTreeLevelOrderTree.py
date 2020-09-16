# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        self.dfs(root, 0, res) # 0 => level
        return res
    
    def dfs(self, root, level, res):     
        if not root:
            return
        
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
        
        
        
        
        
        
        
        
        
        
        