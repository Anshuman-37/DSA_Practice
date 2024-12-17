# Question 20: Three Sum problem: find triplets that sum to zero.

def three_sum_two_pointers(arr):
    arr.sort()
    n = len(arr)
    triplets = []

    for i in range(n - 2):
        # Skip duplicates for the first number
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1
        target = -arr[i]

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for the second number
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets


def three_sum_hash_set(arr):
    arr.sort()
    n = len(arr)
    triplets = set()

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        seen = set()
        target = -arr[i]
        for j in range(i + 1, n):
            complement = target - arr[j]
            if complement in seen:
                triplet = tuple(sorted([arr[i], arr[j], complement]))
                triplets.add(triplet)
            seen.add(arr[j])

    return [list(triplet) for triplet in triplets]


A = [-1, 0, 1, 2, -1, -4]
print(f"Array:{A}")
print(f"Two pointer approach: {three_sum_two_pointers(A)}")
print(f"HashSet approach: {three_sum_hash_set(A)}")

