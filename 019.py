# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, head, n, i):
        if head == None:
            return
        if i+1 == n and head.next != None:
            head.next = head.next.next

        self.helper(head.next, n, i+1)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        copy = head
        while copy!=None:
            length += 1
            copy=copy.next
        if length-n == 0:
            return head.next

        self.helper(head,length-n, 0)

        return head
