# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(r:Optional[TreeNode], i:int)->int:
            if r == None:
                return i

            return max(depth(r.left, i+1),depth(r.right, i+1))


        if root ==None:
            return True


        if abs( depth(root.left, 0)-depth(root.right, 0) ) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
