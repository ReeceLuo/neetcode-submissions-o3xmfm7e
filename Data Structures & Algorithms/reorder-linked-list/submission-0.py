# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        count = 0
        counter = head
        while counter.next:
            counter = counter.next
            count += 1


        mid = head
        for i in range(int(count/2)):
            mid = mid.next
        
        prev = None
        curr = mid.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        mid.next = prev

        p1 = head
        p2 = mid.next

        mid.next = None

        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1
            #temp1.next = temp2

            p1 = temp1
            p2 = temp2


        # p1 = head
        # while count >= 1:
        #     p2 = p1.next
        #     trav = p1
        #     for i in range(count):
        #         trav = trav.next
            
        #     p1.next = trav
        #     trav.next = p2

        #     p1 = p2
        #     count -= 2



