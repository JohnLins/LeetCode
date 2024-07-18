# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helper(self, l1, l2, carry):


        if l1 == None and l2 == None:
            return

        add = (l1.val if l1!=None else 0) + (l2.val if l2!=None else 0) + carry
        print(add)
        if add >= 10:
            carry = add / 10
            add = add%10
        else:
            carry = 0
        l1.val = add


        if (l1.next if l1!=None else None) == None and (l2.next if l2!=None else None) == None and carry != 0:
            print(carry)
            l1.next = ListNode(val=carry)
            return

        if (l2 != None and l2.next != None) and (l1!=None and l1.next == None):
            l1.next = ListNode(val=0)

        self.helper((l1.next if l1!=None else None), (l2.next if l2!=None else None), carry)

    def addTwoNumbers(self, l1, l2):
        self.helper(l1,l2,0)
        return l1

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
