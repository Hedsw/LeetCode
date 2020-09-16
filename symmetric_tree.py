# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.symmetric(root.right, root.left)
    
    def symmetric(self, right, left):
        if right is None and left is None:
            return True
        
        if right is None or left is None:
            return False
        
        if right.val == left.val:
            output = self.symmetric(left.left, right.right)
            inside = self.symmetric(left.right, right.left)
            return output and inside
    
        return False
