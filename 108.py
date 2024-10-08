# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        mid = int(len(nums)/2)
        head = TreeNode(val=nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid+1:])

        return head
