# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p == None and q == None:
                return True

            if q==None or p==None or p.val != q.val:
                return False

            q.right, q.left = q.left, q.right

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        return isSameTree(root.left, root.right)

