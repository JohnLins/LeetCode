# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []
        def traverse(h: Optional[TreeNode]):
            if h == None:
                return

            traverse(h.left)
            trav.append(h.val)
            traverse(h.right)

        traverse(root)
        return trav
