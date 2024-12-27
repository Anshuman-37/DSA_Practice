# Question 8: Find intersection of two arrays using a hash map.
def intersection_of_arrays(arr1, arr2):
    elements = set()
    intersection = []

    for x in arr1:
        elements.add(x)
    for x in arr2:
        if x in elements:
            intersection.append(x)
            elements.remove(x)
    return intersection

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 4, 4, 6]
result = intersection_of_arrays(arr1, arr2)
print(result)