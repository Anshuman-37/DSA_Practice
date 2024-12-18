# Question 27: Median of two sorted arrays.

## Time complexity is O(m+n)
## Space complexity is O(m+n)
def find_median_sorted_arrays_average(nums1, nums2):
    merged = []
    i, j = 0, 0
    m, n = len(nums1), len(nums2)

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    total_length = m + n
    if total_length % 2 == 1:  # IF odd then it's easy to get the average.
        return float(merged[total_length // 2])
    else:  # IF not then get the average between two middle numbers.
        mid1 = merged[total_length // 2 - 1]
        mid2 = merged[total_length // 2]
        return (mid1 + mid2) / 2.0


## The next one is a bit difficult to understand, so I will just post it here
"""
Explanation:
    Smaller Array: We ensure that nums1 is the smaller array to perform binary search on it.
    Binary Search: The while loop performs a binary search on nums1.
    Partitions: partitionX and partitionY divide nums1 and nums2 respectively. half_len is used to calculate partitionY based on partitionX.
    Max/Min: maxLeftX, minRightX, maxLeftY, and minRightY represent the maximum element on the left side and the minimum element on the right side of the partitions in nums1 and nums2.
    Correct Partitions: If maxLeftX <= minRightY and maxLeftY <= minRightX, we have found the correct partitions. The median is calculated based on whether the total length is even or odd.
    Adjust Search: If maxLeftX > minRightY, we need to move the partition in nums1 to the left (reduce partitionX). Otherwise, we move it to the right.
Time Complexity: O(log(min(m,n))). The binary search is performed on the smaller array.
Space Complexity: O(1). We are using a constant amount of extra space.
Edge Cases:
    Empty arrays: The code handles cases where one or both arrays are empty.
    All elements of one array are smaller than the other: The binary search will correctly converge to a partition where one of the partitions is at index 0 or the length of the array.
Duplicate elements: The code handles duplicate elements correctly.
"""

def find_median_sorted_arrays_optimal(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

    m, n = len(nums1), len(nums2)
    low, high = 0, m
    half_len = (m + n + 1) // 2
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = half_len - partitionX

        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
        minRightX = nums1[partitionX] if partitionX < m else float('inf')

        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
        minRightY = nums2[partitionY] if partitionY < n else float('inf')

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Found the correct partitions
            if (m + n) % 2 == 0:  # Even
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:  # Odd
                return float(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return -1

nums1 = [1,3,5,19,25,74]
nums2 = [2,4,18,35,96]

print(find_median_sorted_arrays_optimal(nums1, nums2))