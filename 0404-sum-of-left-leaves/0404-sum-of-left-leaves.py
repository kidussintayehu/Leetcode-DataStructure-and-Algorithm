# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root, left_flag):
            if not root.left and not root.right and left_flag:
                self.total += root.val
            if root.left:
                helper(root.left, True)
            if root.right:
                helper(root.right, False)
            return self.total
                
        if not root:
            return 0
        self.total = 0
        return helper(root, False)