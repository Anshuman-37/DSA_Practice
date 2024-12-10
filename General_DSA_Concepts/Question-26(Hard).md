Question 26: Compare complexity of searching, insertion, and deletion in common data structures.

| Data Structure         | Search Complexity | Insertion Complexity    | Deletion Complexity     |
|------------------------|-------------------|-------------------------|-------------------------|
| Array (unsorted)       | O(n)              | O(1) (at end) or O(n)* | O(n)                    |
| Array (sorted)         | O(log n) (binary search) | O(n) (due to shifting) | O(n) (due to shifting) |
| Singly Linked List     | O(n)              | O(1) (at head)         | O(n) (to find element)  |
| Doubly Linked List     | O(n)              | O(1) (at head/tail)    | O(n) (to find element)  |
| Stack                  | O(n)**            | O(1) (push)            | O(1) (pop)              |
| Queue                  | O(n)**            | O(1) (enqueue)         | O(1) (dequeue)          |
| Binary Search Tree (avg)  | O(log n)     | O(log n)               | O(log n)                |
| Binary Search Tree (worst) | O(n)         | O(n)                   | O(n)                    |
| Balanced BST (e.g. AVL, Red-Black) | O(log n) | O(log n)          | O(log n)                |
| Hash Table (avg)       | O(1)              | O(1)                   | O(1)                    |
| Hash Table (worst)     | O(n)              | O(n)                   | O(n)                    |
| Heap (for min/max)     | O(n)**            | O(log n) (insert)      | O(log n) (remove root)  |

*Insertion in an array at arbitrary positions may require shifting elements, resulting in O(n).  
**Heaps, stacks, and queues generally are not designed for searching arbitrary elements, so searching can be considered O(n) in the general case.
