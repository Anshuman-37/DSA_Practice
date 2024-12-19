# Question 7: Implement Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        # Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive Calls
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements were left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

arr = [5,7,10,1,0,-5,6,23]
print(merge_sort(arr))