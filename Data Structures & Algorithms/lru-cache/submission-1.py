
# for determining which element is LRU, we want O(1) removals. Queue does
# not allow for O(1). Linked list does

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.MRU = ListNode(-1, 0)
        self.LRU = ListNode(-1, 0)
        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # get node. unlink from current position (O(1)), then move to 
        # MRU (O(1))
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.value

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        other = self.MRU.next
        node.next = other
        other.prev = node
        node.prev = self.MRU
        self.MRU.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.add(node)
            return
        
        if len(self.map) >= self.capacity:
            node = self.LRU.prev
            self.remove(node)
            del self.map[node.key]
        
        self.map[key] = ListNode(key, value)
        self.add(self.map[key])
        return




