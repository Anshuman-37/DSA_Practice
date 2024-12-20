# Question 13: Sort an array of 0s and 1s using a two-pointer approach.

def sort_two_elements(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [0,1,0,1,0,1,0,1,0]
print(sort_two_elements(arr))