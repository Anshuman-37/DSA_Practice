# Question 11: Merge two sorted arrays into one sorted array
import heapq

def merge_sorted_arrays_inbuilt(lst1:list, lst2:list) -> list:
    return list(heapq.merge(lst1, lst2))

def merge_sorted_arrays(lst1:list, lst2:list) -> list:
    if not lst1 and not lst2:
        return []
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    n1 = len(lst1)
    n2 = len(lst2)
    i = j = 0
    merged = []
    while i < n1 and j < n2:
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    while i < n1:
        merged.append(lst1[i])
        i += 1
    while j < n2:
        merged.append(lst2[j])
        j += 1
    return merged

lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]

print(f"First sorted array: {lst1}")
print(f"Second sorted array: {lst2}")
print(f"Final sorted array: {merge_sorted_arrays(lst1, lst2)}")
print(f"Using inbuilt function:{merge_sorted_arrays_inbuilt(lst1,lst2)}")
