# Question 30: Find the longest consecutive sequence in an unsorted array.
"""
Explanation:
    Set for Lookup: Create a set num_set from the input array.
    Start of Sequence: Iterate through nums. For each num, check if num - 1 is present in the set. If it's not, then num is the start of a potential consecutive sequence.
    Extend Sequence: Keep incrementing current_num and checking if current_num + 1 is in the set. Update current_length accordingly.
    Update Max: Update max_length with the maximum length found so far.
Time Complexity: O(n). We iterate through the array once, and set operations (add, lookup) take O(1) on average.
Space Complexity: O(n) to store the set.
Edge Cases:
    Empty input array: Returns 0.
"""

def longest_consecutive_optimal(nums):
    num_set = set(nums)  # Convert to set for O(1) lookup
    max_length = 0

    for num in nums:
        if num - 1 not in num_set:  # Check if num is the start of a sequence
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:  # Extend the sequence
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_optimal(nums))
