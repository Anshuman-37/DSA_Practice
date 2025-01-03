
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _remove_tail(self):
        if self.tail.prev == self.head:
            return None
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]
        return lru_node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_tail()
            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.cache[key] = new_node

# Example Usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4)) 