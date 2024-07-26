# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None or k == 0:
            return head

        temp = head
        length = 1
        while temp.next != None:
            temp = temp.next
            length += 1


        temp.next = head



        k = k%length
        focus = head
        for i in range(length - k - 1):
            focus = focus.next

        newhead = focus.next
        focus.next = None

        return newhead

