# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head.next

        pos = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            pos += 1

        if fast:
            l = (pos + 1) * 2
        else:
            l = (pos * 2) + 1

        if l == n:
            return head.next
            
        if pos >= l - n:
            pos = 0
            slow = head

        while pos < l - n - 1:
            slow = slow.next
            pos += 1

        slow.next = slow.next.next

        return head