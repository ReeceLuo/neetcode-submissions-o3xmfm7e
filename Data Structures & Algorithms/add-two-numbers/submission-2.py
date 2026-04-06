# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2

        p3 = ListNode()
        head = p3

        carry = 0
        while p1 or p2 or carry:
            temp = 0
            if p1:
                temp += p1.val
            if p2:
                temp += p2.val
            if carry:
                temp += carry
                carry = 0
            
            if temp >= 10:
                carry = int(temp/10)
                temp %= 10

            p3.next = ListNode(temp, None)
            p3 = p3.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return head.next


