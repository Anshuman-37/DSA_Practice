# Question 22: Separate negative and positive numbers in O(n).

def separate_negative_positive(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while left < right and arr[left] < 0:
            left += 1
        while left < right and arr[right] >= 0:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(separate_negative_positive(arr))