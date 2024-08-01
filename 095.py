# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def  gen(l,r):

            if l==r:
                return [TreeNode(l)]
            if l>r:
                return [None]

            re = []
            for i in range(l,r+1):
                for ltree in gen(l,i-1):
                    for rtree in gen(i+1,r):

                        root = TreeNode(i, ltree, rtree)
                        re.append(root)
            return re

        return gen(1,n)

