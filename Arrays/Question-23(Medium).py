# Question 23: Generate the next permutation of an array.
def next_permutation_optimal(arr):
    n = len(arr)

    # 1. Find the pivot
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # print("The found pivot index",i)
    if i == -1:  # Array is in descending order
        arr.reverse()
        return arr

    # 2. Find the successor
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    # 3. Swap pivot and successor
    arr[i], arr[j] = arr[j], arr[i]

    # 4. Reverse from i+1 to the end
    # print(arr)
    left = i + 1
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

arr = [1,4,3,2]
print(next_permutation_optimal(arr))
