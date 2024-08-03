# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []

        single = True
        if root.left or root.right:
            single = False

        paths = []
        def findpath(node: Optional[TreeNode], path:List[int], total:int)->None:
            total += node.val
            path = path + [node.val]
            if node.left == None and node.right == None:

                if total == targetSum:
                    paths.append(path)
                return
            if node.left:
                findpath(node.left, path, total)
            if node.right:
                findpath(node.right, path, total)
            return

        findpath(root,[],0)


        if single == False and len(paths)==1 and len(paths[0])==1:
            return []
        return paths
