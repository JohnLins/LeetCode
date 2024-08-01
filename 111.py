# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def depth(r: Optional[TreeNode], i:int) -> int:
            if r == None:
                return i+1
            if r.left==None and r.right == None:
                return i+1

            if r.left == None:
                return depth(r.right, i+1)
            if r.right == None:
                return depth(r.left, i+1)

            return min(depth(r.left,i+1), depth(r.right, i+1))

        return depth(root, 0)
