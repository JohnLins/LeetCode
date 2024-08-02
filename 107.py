# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []


        queue = [root]
        ls = []
        while len(queue) != 0:
            vals = []

            for _ in range(len(queue)):
                v = queue.pop(0)
                if v == None:
                    break


                vals.append(v.val)

                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            ls.append(vals)


        return reversed(ls)
