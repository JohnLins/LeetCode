# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(head, last):
            if head.next == None or head.next.next == None:
                if head.next!=None:
                    last.next = head.next
                else:
                    last.next = None
                head.next = last
                return


            newlast = head.next
            temp = head.next.next
            last.next = temp
            head.next = last


            helper(head.next.next, newlast)

        if head == None or head.next == None:
            return head


        store = head.next
        if head.next.next == None:
            first = head
            head.next.next = first
            head.next = None
        else:
            helper(head.next, head)


        return store



