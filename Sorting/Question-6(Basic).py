# Question 6: Sort an array containing only two distinct elements efficiently.

def sort_two_elements(arr, a, b):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == a:
            left += 1
        elif arr[right] == b:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [0,1,0,1,0,1,0,1,0]
print(sort_two_elements(arr, 0, 1))