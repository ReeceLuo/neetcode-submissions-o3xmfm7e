# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        counter = head
        count = 0
        while counter:
            counter = counter.next
            count += 1

        if count == n:
            return head.next

        p1 = head

        for i in range(count - n - 1):
            p1 = p1.next
        
        p1.next = p1.next.next
        return head