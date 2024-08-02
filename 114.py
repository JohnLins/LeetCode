# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return None

        l = []
        def flatten(r:Optional[TreeNode]):
            if r == None:
                return


            l.append(r.val)

            flatten(r.left)

            flatten(r.right)

        flatten(root)



        if l == []:
            return None


        for i in range(0, len(l)):
            root.val = l[i]
            root.left = None
            if root.right!=None:
                root = root.right
            elif i != len(l)-1:


                root.right = TreeNode()
                root = root.right




        """
        Do not return anything, modify root in-place instead.
        """
