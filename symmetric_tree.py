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
        
        return self.symmetricCheck(root.right, root.left) 
    
    def symmetricCheck(self, right, left):
        if right is None and left is None:
            return True
        if right is None or left is None:
            return False
    
        if right.val == left.val:
            outputValue = self.symmetricCheck(right.right, left.left)
            inputValue = self.symmetricCheck(right.left, left.right)
            #print(outputValue and inputValue)
            return outputValue and inputValue
        return False 
        