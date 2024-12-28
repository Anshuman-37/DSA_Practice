def count_subarrays_with_xor_optimal(arr: list[int], target_xor: int) -> int:
    n = len(arr)
    count = 0
    prefix_xor = 0
    xor_freq = {0: 1}

    for num in arr:
        prefix_xor ^= num
        complement_xor = prefix_xor ^ target_xor
        if complement_xor in xor_freq:
            count += xor_freq[complement_xor]
        xor_freq[prefix_xor] = xor_freq.get(prefix_xor, 0) + 1

    return count

arr1 = [4, 2, 2, 6, 4]
target_xor1 = 6
result1 = count_subarrays_with_xor_optimal(arr1, target_xor1)
print(f"Array: {arr1}, Target XOR: {target_xor1}, Count: {result1}")

arr2 = [5, 6, 7, 8, 9]
target_xor2 = 5
result2 = count_subarrays_with_xor_optimal(arr2, target_xor2)
print(f"Array: {arr2}, Target XOR: {target_xor2}, Count: {result2}")

arr3 = [0, 0, 0]
target_xor3 = 0
result3 = count_subarrays_with_xor_optimal(arr3, target_xor3)
print(f"Array: {arr3}, Target XOR: {target_xor3}, Count: {result3}")