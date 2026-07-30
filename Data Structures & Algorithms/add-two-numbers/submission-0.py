# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        s = 0
        while l1 and l2:
            s += l1.val + l2.val
            cur.next = ListNode(s % 10)
            l1, l2, cur = l1.next, l2.next, cur.next
            s //= 10
        while l1:
            s += l1.val
            cur.next = ListNode(s % 10)
            l1, cur = l1.next, cur.next
            s //= 10
        while l2:
            s += l2.val
            cur.next = ListNode(s % 10)
            l2, cur = l2.next, cur.next
            s //= 10
        if s > 0:
            cur.next = ListNode(s)
        return dummy.next