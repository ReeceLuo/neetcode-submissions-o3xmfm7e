# if at capacity, evict least recently used (LRU) key 
# use linked list?

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = {}

        # left is for LRU, right is for MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    # insert node at right (MRU)
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.nums:
            return -1 
        self.remove(self.nums[key]) # remove node from list
        self.insert(self.nums[key]) # add to right as MRU
        return self.nums[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.nums:
            self.remove(self.nums[key])
        self.nums[key] = Node(key, value)
        self.insert(self.nums[key])

        if len(self.nums) > self.capacity:
            # remove LRU (left) from list and nums
            LRU = self.left.next
            self.remove(LRU)
            del self.nums[LRU.key]