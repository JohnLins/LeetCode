# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def trav(r: Optional[TreeNode], level) -> List[List[int]]:
            if r == None:
                return
            print(r.val)
            if level not in levels.keys():
                levels[level] = [r.val]
            else:
                levels[level].append(r.val)


            trav(r.left, level+1)
            trav(r.right, level+1)


        trav(root,0)
        output = []
        for i in levels.keys():
            output.append(levels[i])

        return output

