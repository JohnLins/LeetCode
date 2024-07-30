# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftd = ListNode(0)
        rightd = ListNode(0)

        leftptr = leftd
        rightptr = rightd
        xptr = head
        while xptr != None:
            if xptr.val < x:
                leftptr.next = xptr
                leftptr = leftptr.next
            else:
                rightptr.next = xptr
                rightptr = rightptr.next

            xptr = xptr.next

        rightptr.next = None
        leftptr.next = rightd.next


        return leftd.next
