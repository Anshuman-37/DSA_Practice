# Question 25: Design a hash map from scratch (with collision resolution and resizing).
class OptimalHashMap:
    def __init__(self, initial_capacity=10, load_factor=0.75):
        self.capacity = initial_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.load_factor = load_factor

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

    def _resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = new_buckets
        self.size = 0  # Reset size as we're re-inserting

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)


hm = OptimalHashMap(initial_capacity=5)
hm.put("apple", 1)
hm.put("banana", 2)
hm.put("cherry", 3)
hm.put("date", 4)
hm.put("elderberry", 5)
hm.put("fig", 6)  # This might trigger a resize

print(f"Get 'banana': {hm.get('banana')}")
print(f"Get 'grape': {hm.get('grape')}")

hm.remove("banana")
print(f"Get 'banana' after removal: {hm.get('banana')}")

print(f"HashMap size: {hm.size}")
print(f"HashMap capacity: {hm.capacity}")

# Example showing resizing
hm2 = OptimalHashMap(initial_capacity=2)
hm2.put("a", 1)
hm2.put("b", 2)
print(f"hm2 capacity after 2 puts: {hm2.capacity}")
hm2.put("c", 3)
print(f"hm2 capacity after 3 puts: {hm2.capacity}")