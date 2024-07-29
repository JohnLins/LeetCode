# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rec(root, low, high):

            if root == None:
                return True


            if root.val <= low or root.val >= high:
                return False

            if ((root.right == None or root.right.val > root.val) and (root.left == None or root.left.val < root.val) and rec(root.right, root.val, high) and rec(root.left, low, root.val)):
                return True

        return rec(root, float("-inf"), float("inf"))
