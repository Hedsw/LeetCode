# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''           
class Solution:
    def isValidBST(self, root):
        
        output = []
        
        self.inorder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True
    
    def inorder(self, root, output):
        if not root:
            return 
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
'''        
class Solution:
    def isValidBST(self, root):
        return self.validcheck(root, float('-inf'), float('inf'))
    
    def validcheck(self, root, left, right):
        if not root:
            return True
        
        if not left < root.val < right:
            return False
        
        return self.validcheck(root.left, left, root.val) and self.validcheck(root.right, root.val, right)
        
        