# Question 4 Implement Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    # Iterate through the array starting from the second element
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the last element in the sorted portion

        # Move elements of the sorted portion that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key into its correct position
        arr[j + 1] = key

    return arr

arr = [5,4,3,2,1]
print(insertion_sort(arr))