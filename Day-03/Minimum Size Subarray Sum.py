# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # If either list is empty, there is no intersection
        if not headA or not headB:
            return None

        # Two pointers for both lists
        pointerA, pointerB = headA, headB

        # Traverse both lists. When a pointer reaches the end,
        # move it to the start of the other list.
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # They either meet at the intersection or both become None
        return pointerA
