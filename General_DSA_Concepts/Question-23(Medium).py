# Question 23: Implement a hash table using chaining.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key '{key}' with new value '{value}' in bucket {index}.")
                return
        self.table[index].append([key, value])
        print(f"Inserted key '{key}' with value '{value}' into bucket {index}.")

    def search(self, key):
        index = self._hash(key)
        print(f"Searching for key '{key}' in bucket {index}.")
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key '{key}' found with value '{pair[1]}'.")
                return pair[1]
        print(f"Key '{key}' not found.")
        return None

    def delete(self, key):
        index = self._hash(key)
        print(f"Attempting to delete key '{key}' from bucket {index}.")
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Key '{key}' deleted from bucket {index}.")
                return True
        print(f"Key '{key}' not found. Deletion failed.")
        return False

    def display(self):
        print("Current state of the hash table:")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
    ht = HashTable(size=5)

    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    ht.insert("grape", 4)
    ht.insert("melon", 5)

    ht.display()

    ht.search("apple")
    ht.search("cherry")

    ht.insert("apple", 10)
    ht.display()

    ht.delete("banana")
    ht.display()

    ht.delete("cherry")
