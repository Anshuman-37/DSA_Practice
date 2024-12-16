# Question 16: Sort an array of 0s, 1s, and 2s (Dutch National Flag problem).

def sort_array_dutch_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
print(f"The array is:{arr}")
print(f"Sorted array is{sort_array_dutch_flag(arr)}")