# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = head
        last = head
        def removedups(h, last):
            if last == None or h == None:
                return

            if h.val == last.val:
                last.next = h.next
            else:
                last = h


            return removedups(h.next, last)

        if head == None or head.next == None:
            return store

        removedups(head.next, last)

        return store

