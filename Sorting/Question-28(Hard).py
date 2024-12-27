"""
K-Way Merge
The k-way merge algorithm is crucial for efficiently merging multiple sorted files. Here's how it works:
    Read Buffers: Allocate a small input buffer for each of the k sorted files and an output buffer.
    Initial Read: Read a portion of data from each file into its corresponding input buffer.
    Min-Heap: Create a min-heap of size k, where each element in the heap represents the smallest element currently in the input buffer of a file. The heap stores pairs of (value, file_index).

    Iterative Merging:
        Extract the minimum element (along with its file index) from the min-heap.
        Write the extracted element to the output buffer.
        Read the next element from the corresponding file into its input buffer. If the buffer is empty, read the next chunk from the file.
        Insert the newly read element into the min-heap.
        Repeat until all input buffers are empty and the min-heap is empty.

    Output Buffer Management: When the output buffer is full, write its contents to the output file and clear the buffer.

Illustrative Example
    Let's say you have 4 sorted files (F1, F2, F3, F4) and a min-heap:
    Initial State:
        F1: [5, 10, 15, ...] (Buffer: [5, 10])
        F2: [2, 8, 12, ...] (Buffer: [2, 8])
        F3: [7, 9, 20, ...] (Buffer: [7, 9])
        F4: [1, 4, 11, ...] (Buffer: [1, 4])
    Min-Heap: [(1, F4), (2, F2), (5, F1), (7, F3)]

    Iteration 1:
        Extract (1, F4) from the heap.
        Write 1 to the output buffer.
        Read 4 from F4 into its buffer.
        Insert (4, F4) into the heap.
        Min-Heap: [(2, F2), (4, F4), (5, F1), (7, F3)]

    Iteration 2:
        Extract (2, F2) from the heap.
        Write 2 to the output buffer.
        Read 8 from F2 into its buffer.
        Insert (8, F2) into the heap.
        Min-Heap: [(4, F4), (5, F1), (7, F3), (8, F2)]
...and so on, until all files are merged.
"""
