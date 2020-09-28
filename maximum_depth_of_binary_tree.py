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
        # This is new version
        if not root:
            return 0
        
        array = [root]
        depth = 0
        
        while array:
            depth += 1
            queue = []
            for i in array:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
                array = queue
        return depth