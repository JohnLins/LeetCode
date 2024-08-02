# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder)==0 or len(inorder)==0:
            return None

        root=TreeNode(preorder[0])
        i=0

        for j in range(len(inorder)):
            if inorder[j] == preorder[0]:
                i = j
                break


        root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
