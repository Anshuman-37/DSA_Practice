# Question 10: Check if a subarray with sum 0 exists (use hashing).

def subarray_sum_zero(arr):
    seen_sums = set()
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

arr1 = [4, 2, -3, 1, 6]
print(subarray_sum_zero(arr1))

arr2 = [4, 2, 0, 1, 6]
print(subarray_sum_zero(arr2))

arr3 = [-3, 2, 3, 1, 6]
print(subarray_sum_zero(arr3))

arr4 = [1, -1]
print(subarray_sum_zero(arr4))

arr5 = [0, 0]
print(subarray_sum_zero(arr5))