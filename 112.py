# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False

        def path(r: Optional[TreeNode], total)->bool:
            if r != None:
                total += r.val
            if r == None:
                return False
            if total == targetSum and (r.left == None and r.right==None):
                return True
            if r != None:
                return path(r.left, total) or path(r.right, total)

            return False

        return path(root, 0)
