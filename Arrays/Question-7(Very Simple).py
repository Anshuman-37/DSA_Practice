# Question - 7: Remove duplicates from a sorted array in-place.

def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    del nums[write_index:]
    return write_index

sorted_array = [1, 1, 2, 3, 3, 4, 5, 5, 5]
unique_count = remove_duplicates(sorted_array)
print(f"Unique count: {unique_count}")
print(f"Array after removing duplicates: {sorted_array}")


