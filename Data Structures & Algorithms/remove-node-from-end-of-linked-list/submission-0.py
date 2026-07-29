# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        i = 0
        slow = fast = dummy
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        if i >= n:
            slow.next = slow.next.next
        return dummy.next