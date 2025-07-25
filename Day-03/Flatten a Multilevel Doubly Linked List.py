class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dummy = Node(0)   # Dummy node to simplify linking
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()

    
            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr  

        
        dummy.next.prev = None
        return dummy.next
