# Question 27: Implement a parallelized version of merge sort.

"""
Understanding Parallel Merge Sort
The basic idea behind parallelizing Merge Sort is to divide the sorting task among multiple processes (or threads) that can run concurrently. Here's a high-level overview:

Divide: Split the input array into multiple subarrays.
Conquer (in Parallel): Sort each subarray in a separate process.
Combine (Merge): Merge the sorted subarrays together. This step can also be parallelized to some extent, but it's inherently more sequential than the sorting step.
"""
