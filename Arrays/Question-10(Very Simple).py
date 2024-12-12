def find_second_largest(nums):
    if not nums or len(nums) < 2:
        raise ValueError("Array must contain at least two elements.")

    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        raise ValueError("No second largest element found.")

    return second


def find_second_largest_sorting(nums):
    if not nums or len(nums) < 2:
        raise ValueError("Array must contain at least two elements.")

    sorted_nums = sorted(nums, reverse=True)

    # Traverse the sorted array to find the second distinct element
    first = sorted_nums[0]
    for num in sorted_nums[1:]:
        if num != first:
            return num

    raise ValueError("No second largest element found.")


lst = [12, 35, 1, 10, 34, 1]
print(f"The second largest element is: {find_second_largest(lst)}")
print(f"The second largest element is: {find_second_largest_sorting(lst)}")