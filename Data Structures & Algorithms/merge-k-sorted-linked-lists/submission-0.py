# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while None in lists:
            lists.remove(None)
        dummy = ListNode(-1)
        cur = dummy
        while lists:
            minVal, minAt = float('inf'), -1
            for i in range(len(lists)):
                if lists[i].val < minVal:
                    minVal = lists[i].val
                    minAt = i
            cur.next = lists[minAt]
            cur = cur.next
            lists[minAt] = lists[minAt].next
            if not lists[minAt]:
                lists.pop(minAt)
        return dummy.next