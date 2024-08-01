# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        cur = root
        prev = None
        rep = []
        s = []

        while cur != None or s != []:
            while cur != None:
                s.append(cur)
                cur = cur.left

            temp = s.pop()

            if prev != None and temp.val < prev.val:
                rep.append([prev, temp])
            prev = temp
            cur = temp.right


        rep[0][0].val, rep[-1][-1].val = rep[-1][-1].val, rep[0][0].val

        """
        Do not return anything, modify root in-place instead.
        """
