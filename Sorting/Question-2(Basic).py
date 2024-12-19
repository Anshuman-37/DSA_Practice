# Question 2: Implement Bubble Sort.


## Time Complexity O(n^2)
## Space Complexity O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [5,4,3,2,1]
print(bubbleSort(arr))