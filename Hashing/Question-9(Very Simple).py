# Question 9: First element that appears k times in an array.

def first_element_k_times(arr, k):
    counts = {}

    for x in arr:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] == k:
            return x

    return -1

arr1 = [1, 7, 4, 3, 4, 8, 7, 4]
k1 = 3
print(first_element_k_times(arr1, k1))

arr2 = [4, 1, 6, 1, 6, 4, 4, 6]
k2 = 2
print(first_element_k_times(arr2, k2))

arr3 = [1, 2, 3]
k3 = 2
print(first_element_k_times(arr3, k3))