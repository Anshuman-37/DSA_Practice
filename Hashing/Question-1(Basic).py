# Question 1: Understand the concept of a hash map and hashing.

"""
What is Hashing?
    Hashing is the process of transforming a given key into an index (a numerical value) using a hash function. This index is then used to determine where the key-value pair should be stored in the hash map's underlying array.

Key Concepts
    Hash Function:
        Takes a key as input.
        Returns an integer value (the hash code or hash value) within a specific range.
        Ideally, a good hash function should:
            Be deterministic: The same key should always produce the same hash code.
            Be efficient to compute.
            Distribute keys uniformly: It should spread the keys evenly across the available buckets to minimize collisions (explained below).
            Minimize collisions: Different keys should ideally produce different hash codes (though this is not always possible).

    Buckets:
        The underlying array of a hash map is divided into buckets.
        Each bucket can store one or more key-value pairs.

    Collisions:
        A collision occurs when two different keys produce the same hash code, meaning they map to the same bucket.
        Collisions are inevitable in most cases because the number of possible keys is usually much larger than the number of buckets.
        Hash maps have mechanisms to handle collisions (see below).
        Collision Resolution Techniques
        Since collisions are unavoidable, hash maps need strategies to deal with them. Here are two common techniques:

    Separate Chaining:
        Each bucket stores a linked list (or another dynamic data structure) of key-value pairs.
        When a collision occurs, the new key-value pair is added to the linked list of the corresponding bucket.

    Lookup: To find a key, you hash the key, go to the corresponding bucket, and then traverse the linked list to find the key.

    Open Addressing:
        When a collision occurs, the algorithm probes (searches) for the next available empty slot in the array, using a predefined sequence of locations.
            Linear Probing: The simplest open addressing technique. It checks the next consecutive slot until an empty one is found.
            Quadratic Probing: Uses a quadratic function to determine the next slot to probe.
            Double Hashing: Uses a second hash function to determine the probing interval.

Example (Conceptual)
    Let's say you have a hash map with 5 buckets (indices 0 to 4) and the following hash function:

    hash(key) = key % 5 (where % is the modulo operator)

    Insert (12, "apple"):
        hash(12) = 12 % 5 = 2

    The key-value pair (12, "apple") is stored in bucket 2.

    Insert (7, "banana"):
        hash(7) = 7 % 5 = 2

    Collision! Bucket 2 is already occupied.
        Separate Chaining: (12, "apple") and (7, "banana") would be stored in a linked list in bucket 2.
        Open Addressing (Linear Probing): We would check bucket 3, then bucket 4, and so on, until an empty slot is found.
            Lookup (7):
            hash(7) = 7 % 5 = 2
            Go to bucket 2.
        Separate Chaining: Traverse the linked list in bucket 2 to find the key 7.
        Open Addressing: Start probing from bucket 2 based on the chosen probing strategy until you find the key 7 or an empty slot.

    Time Complexity (Average Case)
        Insertion: O(1)
        Deletion: O(1)
        Lookup: O(1)
"""
