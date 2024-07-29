# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        valswithdups = set()
        def removedups(head: Optional[ListNode], valswithdups) -> Optional[ListNode]:
            store = head
            last = head
            def removedup(h, last):
                if last == None or h == None:
                    return

                if h.val == last.val:
                    valswithdups.add(h.val)
                    last.next = h.next
                else:
                    last = h


                return removedup(h.next, last)

            if head == None or head.next == None:
                return store

            removedup(head.next, last)

            return store



        temp = head
        ptr = head
        while ptr != None:
            minval = ptr.val
            minptr = ptr
            forwardptr = ptr
            while forwardptr != None:
                if forwardptr.val < minval:
                    minval = forwardptr.val
                    minptr = forwardptr
                forwardptr = forwardptr.next
            minptr, ptr = ptr, minptr

            ptr = ptr.next
        removedups(temp, valswithdups)

        valswithdups = sorted(list(valswithdups))
        print(valswithdups)
        tempptr = temp
        lasttemp = None
        i = 0
        while tempptr != None:

            if i < len(valswithdups) and tempptr.val == valswithdups[i]:


                #del
                if lasttemp == None:
                    print(valswithdups[i], tempptr.val, "-")
                    temp = temp.next
                else:
                    print(valswithdups[i], tempptr.val, "+")
                    lasttemp.next = tempptr.next
                i += 1

            else:
                lasttemp = tempptr
            tempptr = tempptr.next


        return temp
