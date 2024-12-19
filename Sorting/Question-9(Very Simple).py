# Question 9: Implement Count Sort for a limited range k

def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for x in arr:
        count[x - min_val] += 1

    for i in range(1, range_val):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

arr2 = [0, 5, 2, 1, 8, 0, 6]
sorted_arr2 = counting_sort(arr2)
print("Sorted array:", sorted_arr2)