# Question 16: Sort one array according to the order defined by another array.

"""
Explanation:
    order_map: A dictionary where keys are elements from arr2 and values are their indices.
    custom_comparator(x):
    If x is in order_map, it returns a tuple (order_map[x], -1). The first element of the tuple is the index of x in arr2 (used for sorting according to arr2's order). The second element, -1, is used to ensure that elements present in arr2 are prioritized over elements not in arr2 during sorting.
    If x is not in order_map, it returns a tuple (len(arr2), x). The first element, len(arr2), ensures that elements not in arr2 are placed after all elements that are in arr2. The second element, x, is used to sort these remaining elements in ascending order.
    sorted(arr1, key=custom_comparator): Sorts arr1 using the custom_comparator to determine the order.
Time Complexity: O(n log n), where n is the length of arr1 (due to sorting).
Space Complexity: O(m), where m is the length of arr2 (to store the order_map).
"""
def sort_by_other_array(arr1, arr2):
    order_map = {val: i for i, val in enumerate(arr2)}  # Create index map for arr2
    print(order_map)
    def custom_comparator(x):
        if x in order_map:
            return order_map[x], -1  # -1 to prioritize elements in arr2
        else:
            return len(arr2), x  # Elements not in arr2 come after, sorted by value

    return sorted(arr1, key=custom_comparator)

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]


print(sort_by_other_array(arr1, arr2))