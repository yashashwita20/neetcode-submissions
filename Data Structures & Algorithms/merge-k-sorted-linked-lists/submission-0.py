# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        n = len(lists)

        if n == 0: return None
        if n == 1: return lists[0]
        
        def mergeTwoLists(list1, list2):
            if not list1: return list2
            if not list2: return list1
            if not list1 and not list2: return None

            head = ListNode()
            curr = head

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next

            curr.next = list1 or list2

            return head.next

        for i in range(1,n):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])

        return lists[n-1]

        
        