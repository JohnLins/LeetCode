# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lengthptr = head
        length = 0
        while lengthptr != None:
            length+=1
            lengthptr = lengthptr.next




        def cons(r: Optional[ListNode], t: Optional[TreeNode], l: int) -> Optional[TreeNode]:
            if r == None or l == 0:
                return None
            if l == 1:
                print(r.val)
                return TreeNode(r.val)


            ptr = r
            firsthalf = ptr
            for i in range(int(l/2)):

                ptr=ptr.next
            t.val = ptr.val


            secondhalf = ptr.next
            ptr = None

            t.left = cons(firsthalf, TreeNode(), int(l/2))
            t.right = cons(secondhalf, TreeNode(), int(l/2)  if l%2 != 0 else int(l/2)-1)
            return t



        return cons(head, TreeNode(), length)

