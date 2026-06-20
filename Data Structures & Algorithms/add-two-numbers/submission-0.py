# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_ = 0
        carry = 0

        curr = ListNode()
        head = curr

        while l1 or l2:

            sum_ = carry

            if l1:
                sum_ += l1.val
                l1 = l1.next

            if l2:
                sum_ += l2.val
                l2 = l2.next

            carry = sum_ // 10
            sum_ = sum_ % 10

            curr.val = sum_

            if l1 or l2 or carry:
                curr.next = ListNode(carry, None)
                curr = curr.next

        return head