# Question 24: Sort array by parity (evens first, then odds)
def sort_by_parity(arr):
    n = len(arr)
    low = 0
    high = n - 1
    while low < high:
        if arr[low] % 2 == 1:
            if arr[high] % 2 == 0:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1
    return arr

arr = [5,7,2,12,1,6,19]
print(sort_by_parity(arr))