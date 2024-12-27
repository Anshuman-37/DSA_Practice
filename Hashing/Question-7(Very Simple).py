# Question 7: Check if two arrays are disjoint using a hash map.
def are_disjoint(arr1, arr2):
    elements = set()
    for x in arr1:
        elements.add(x)
    for x in arr2:
        if x in elements:
            return False
    return True

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(are_disjoint(arr1, arr2))