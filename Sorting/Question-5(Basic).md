## Time Complexities of Bubble, Selection, and Insertion Sort

Here's a breakdown of the time complexities for Bubble Sort, Selection Sort, and Insertion Sort:

**1. Bubble Sort:**

*   **Best Case:** O(n) - Occurs when the input array is already sorted. The algorithm only needs to make one pass through the array to confirm this.
*   **Average Case:** O(n^2) - Occurs when the input array is randomly ordered.
*   **Worst Case:** O(n^2) - Occurs when the input array is sorted in reverse order.

**Explanation:** Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. In the worst and average cases, it requires n-1 passes through the array, and in each pass, it makes up to n-1 comparisons. This results in a quadratic time complexity.

**2. Selection Sort:**

*   **Best Case:** O(n^2)
*   **Average Case:** O(n^2)
*   **Worst Case:** O(n^2)

**Explanation:** Selection sort works by repeatedly finding the minimum element from the unsorted part and putting it at the beginning. It performs n-1 passes, and in each pass, it needs to compare the current element with the remaining unsorted elements. This gives it a consistent quadratic time complexity regardless of the initial order of the input.

**3. Insertion Sort:**

*   **Best Case:** O(n) - Occurs when the input array is already sorted.
*   **Average Case:** O(n^2)
*   **Worst Case:** O(n^2) - Occurs when the input array is sorted in reverse order.

**Explanation:** Insertion sort works by taking elements from the unsorted part and inserting them into their correct position in the sorted part. In the best case, when the array is already sorted, only one comparison is needed in each iteration. However, in the worst and average cases, it may need to make up to n-1 comparisons and shifts for each element, leading to a quadratic time complexity.

**Summary Table:**

| Sorting Algorithm | Best Case | Average Case | Worst Case |
|-------------------|-------------|--------------|-------------|
| Bubble Sort      | O(n)        | O(n^2)       | O(n^2)      |
| Selection Sort   | O(n^2)      | O(n^2)       | O(n^2)      |
| Insertion Sort   | O(n)        | O(n^2)       | O(n^2)      |

In general, for large datasets, these sorting algorithms are less efficient than algorithms with O(n log n) time complexity, such as Merge Sort or Quick Sort. However, Insertion sort can be efficient for small datasets or nearly sorted datasets.