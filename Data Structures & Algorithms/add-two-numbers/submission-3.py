# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create new node for each
        # if sum of digits exceeds 10, carry over the 1
        # use while loop for while either list is valid.

        dummy = curr = ListNode()

        carry = False
        while l1 or l2 or carry:
            currSum = 0
            if l1:
                currSum += l1.val
            if l2:
                currSum += l2.val
            if carry:
                currSum += 1
                carry = False
            if currSum >= 10:
                carry = True
                currSum = currSum % 10
            
            curr.next = ListNode(currSum)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

        



        
        