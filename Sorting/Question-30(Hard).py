# Question 30: Sort elements by their absolute difference with a given value.

def sort_by_absolute_difference(arr, target):
    return sorted(arr, key=lambda x: abs(x - target))

arr = [10, 5, 3, 9, 2]
target = 7
sorted_arr = sort_by_absolute_difference(arr, target)
print("Sorted array:", sorted_arr)