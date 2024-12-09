### Explain collision handling in hashing

#### Chaining

Chaining is a collision resolution technique where each slot in the hash table points to a secondary data structure (
commonly a linked list) that holds all elements hashing to the same index.

##### How it works?

* **Hash Function**: A key is passed through a hash function to compute its index in the hash table.
* **Insertion**:
    * If the computed index is empty, the key is inserted directly.
    * If the index already contains one or more keys (a collision), the new key is added to the linked list (or another
      secondary structure) at that index.
* **Search**:
    * The hash function computes the index.
    * The linked list at that index is traversed to find the desired key.
* **Deletion**:
    * The Similar to search, locate the key in the linked list and remove it.

#### Advantages

* Simplicity: Easy to implement, especially with linked lists.
* Dynamic Size: Can handle an arbitrary number of collisions without a fixed limit, limited only by memory.
* Performance: Performance degrades gracefully as the load factor increases.

#### Open Addressing

Open Addressing is a collision resolution strategy where, upon a collision, the algorithm probes the hash table to find
another vacant slot based on a probing sequence. All elements are stored directly within the hash table without using
secondary data structures.

* Linear Probing:
    * Probing Sequence: Sequentially check the next slot (i.e., index + 1, index + 2, …) until an empty slot is found.
    * Pros: Simple to implement.
    * Cons: Suffers from primary clustering, where groups of occupied slots form, leading to longer probe sequences.

* Quadratic Probing:
    * Probing Sequence: Use a quadratic function to determine the step size (e.g., index + 1², index + 2², index +
      3², …).
    * Pros: Reduces primary clustering compared to linear probing.
    * Cons: Can still experience secondary clustering and might not probe all slots unless the table size is chosen
      carefully.

* Double Hashing:
    * Probing Sequence: Use a second hash function to determine the step size (e.g., index + i * h₂(key), where h₂ is a
      different hash function and i is the probe attempt number).
    * Pros: Minimizes clustering and provides a more uniform probe sequence.
    * Cons: More complex to implement due to the need for a second hash function.

#### Operations

* Insertion:
    * Compute the initial index using the primary hash function.
    * If the slot is occupied, use the probing sequence to find the next available slot.
    * Insert the key in the found slot.

* Search:
    * Compute the initial index.
    * If the key at that index matches, return it.
    * If not, follow the probing sequence until the key is found or an empty slot is encountered (indicating the key is
      not
      present).

* Deletion:
    * Locate the key using the search process.
    * Remove the key and handle the vacancy using techniques like lazy deletion (marking the slot as deleted) to ensure
      the
      integrity of probe sequences for other keys.

#### Advantages
* Space Efficiency: Does not require additional data structures beyond the hash table itself.
* Cache Performance: Better cache locality since data is stored contiguously.
* Avoids Pointers: Eliminates the need for extra pointers, reducing memory overhead.

#### Disadvantages
* Clustering Issues: Especially with linear probing, clustering can degrade performance.
* Load Factor Sensitivity: Performance deteriorates significantly as the load factor approaches 1; often, load factors are kept below 0.7.
* Deletion Complexity: Removing elements can complicate the probing process and may require special handling.