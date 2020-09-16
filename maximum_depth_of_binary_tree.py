# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        '''
        
        if not root:
            return 0
        depth = 0
        level = [root] if root else []
        
        while level:
            depth += 1
            queue = []
            
            for i in level:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
                level = queue
        return depth