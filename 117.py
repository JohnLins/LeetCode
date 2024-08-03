"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None

        queue = [root]

        while len(queue) != 0 :
            prev = None

            for i in range(len(queue)):
                v = queue.pop(0)


                if prev:
                    prev.next = v
                prev = v

                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)

            if prev:
                prev.next = None

        return root
