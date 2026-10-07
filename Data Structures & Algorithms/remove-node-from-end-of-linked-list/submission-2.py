# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove nth node from end
        # must get length of list

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        if n == length:
            return head.next

        curr = head
        for i in range(length - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head




