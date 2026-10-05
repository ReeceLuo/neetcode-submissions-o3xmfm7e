# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # to get sorted list, must get smallest value from three
        # each list is sorted so we can start with their heads
        # to get smallest among these values, add heads to heap.
        # each time we take val -> add next val in list
        # merge - no creation

        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (NodeWrapper(head)))

        curr = dummy = ListNode()
        while heap:
            node_wrapper = heapq.heappop(heap)
            curr.next = node_wrapper.node
            curr = curr.next
            if node_wrapper.node.next:
                heapq.heappush(heap, (NodeWrapper(node_wrapper.node.next)))

        return dummy.next






