# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        leftp = None
        rightp = None
        i = 1
        while head!=None:
            if i == left:
                leftp = head
            if i == right:
                rightp = head
            head = head.next
            i+=1


        def rev(lptr: Optional[ListNode],rptr: Optional[ListNode], left: int, right: int) -> None:


            if lptr == None or rptr == None or left >= right:
                return

            lptr.val, rptr.val = rptr.val, lptr.val

            if right-1 == left:
                return

            newright = lptr
            k = left
            while k < right-1:

                newright=newright.next
                k+=1



            rev(lptr.next, newright, left+1,right-1)




        rev(leftp, rightp,left, right)
        return temp
