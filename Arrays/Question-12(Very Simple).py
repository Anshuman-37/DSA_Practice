# Question 12: Find the kth smallest element in an unsorted array.
# The speed can be increased using Quick Select algorithm to O(n) on average.

def k_smallest_element(lst:list, k:int) -> int:
    if k > len(lst):
        return -1
    lst.sort()
    return lst[k-1]

lst = [7, 10, 4, 3, 20, 15]
k = 3

print(f"Array: {lst}")
print(f"{k}th smallest element: {k_smallest_element(lst, k)}")

