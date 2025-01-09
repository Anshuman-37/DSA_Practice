"""
Min-Heap and Max-Heap Explained
Both min-heap and max-heap are specific types of binary heaps, which are tree-based data structures that satisfy the heap property. They are crucial for implementing priority queues and are used in various algorithms like heap sort. The primary difference lies in the ordering of elements.

1. Min-Heap:
    A min-heap is a binary tree where the value of each node is less than or equal to the value of its children. This property ensures that the smallest element in the heap is always at the root of the tree.
    Properties of a Min-Heap:
        Min-Heap Property: For every node i other than the root, parent(i) <= A[i], where A is the array representation of the heap. This means the value of the parent node is always less than or equal to the value of its children.
        Smallest Element at the Root: Due to the min-heap property, the root node always contains the smallest element in the entire heap.
        Shape Property: A min-heap is a complete binary tree. This means that all levels of the tree are fully filled, except possibly the last level, which is filled from left to right. This property allows for efficient array-based implementation.
        No Ordering Among Siblings: While parents have a defined relationship with their children, there's no specific ordering between sibling nodes. The left child can be larger or smaller than the right child.
        Height of the Heap: For a heap with n nodes, the height is approximately log₂(n). This logarithmic height contributes to the efficiency of heap operations.

2. Max-Heap:
    A max-heap is a binary tree where the value of each node is greater than or equal to the value of its children. This property ensures that the largest element in the heap is always at the root of the tree.
    Properties of a Max-Heap:
        Max-Heap Property: For every node i other than the root, parent(i) >= A[i], where A is the array representation of the heap. This means the value of the parent node is always greater than or equal to the value of its children.
        Largest Element at the Root: Due to the max-heap property, the root node always contains the largest element in the entire heap.
        Shape Property: Like the min-heap, a max-heap is also a complete binary tree.
        No Ordering Among Siblings: Similar to min-heaps, there's no specific ordering between sibling nodes in a max-heap.
        Height of the Heap: The height of a max-heap with n nodes is also approximately log₂(n).

Key Differences between Min-Heap and Max-Heap:

    Feature	Min-Heap	Max-Heap
    Heap Property	Parent's value <= Child's value	Parent's value >= Child's value
    Root Element	Smallest element in the heap	Largest element in the heap
    Use Cases	Finding the minimum, priority queues (for retrieving smallest elements first)	Finding the maximum, priority queues (for retrieving largest elements first)
    Implementation Notes:

    Both min-heaps and max-heaps are often implemented using arrays. Given a node at index i:
        Parent Index: floor((i-1)/2)
        Left Child Index: 2*i + 1
        Right Child Index: 2*i + 2

    In Summary:
    Min-heaps and max-heaps are essential data structures for maintaining order within a collection. Min-heaps prioritize access to the smallest element, while max-heaps prioritize access to the largest element. Their logarithmic height and efficient operations make them valuable tools in various algorithms and applications.

"""
