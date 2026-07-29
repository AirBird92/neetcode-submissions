# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        prev, cur = None, head2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        cur1, cur2 = head, prev
        while cur2:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1, cur2 = temp1, temp2