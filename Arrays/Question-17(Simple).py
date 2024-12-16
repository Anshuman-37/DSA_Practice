# Question 17: Find the majority element (more than n/2 occurrences).

def voting_boyer_mayer(arr):
    # Candidate Selection
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    # Check whether the candidate is the majority element
    if count is not None:
        count = arr.count(candidate)
        if count > len(arr) // 2:
            return candidate
    return -1

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(f"Array: {arr}")
print(f" Majority element is {voting_boyer_mayer(arr)}")