# Question 2: Insert and retrieve elements in a hash map.

class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def __len__(self):
        return self.size

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        return None

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

my_hash_map = HashMap()

my_hash_map.insert("apple", 1)
my_hash_map.insert("banana", 2)
my_hash_map.insert("cherry", 3)
my_hash_map["grape"] = 4

print(my_hash_map.get("banana"))
print(my_hash_map["apple"])
print(my_hash_map.get("mango"))

print(len(my_hash_map))

try:
    print(my_hash_map["mango"])
except KeyError as e:
    print(f"KeyError: {e}")
    
