"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # one pass to create each node
        # use hash table to store index?

        dummy = curr = Node(0)
        node_map = {}

        # build list (w/o random)
        og_curr = head
        while og_curr:
            curr.next = Node(og_curr.val)
            curr = curr.next
            node_map[og_curr] = curr
            og_curr = og_curr.next

        curr = dummy.next
        og_curr = head
        while curr:
            if og_curr.random:
                curr.random = node_map[og_curr.random]
            curr, og_curr = curr.next, og_curr.next
        
        return dummy.next





