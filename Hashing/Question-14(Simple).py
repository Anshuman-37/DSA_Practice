# Question 14: Longest substring without repeating characters using a hash map.

"""
Initialization:
    n = len(s): We get the length of the input string s and store it in n. This is useful for iterating through the string.
    max_len = 0: This variable will store the length of the longest substring found so far. We initialize it to 0.
    start = 0: This is the starting index of our sliding window. Initially, the window starts at the beginning of the string.
    char_index_map = {}: This is our hash map (dictionary in Python). It will store characters as keys and their most
    recent index in the string as values. This allows us to quickly check if a character has been seen before and
    where it was last seen.

Sliding Window Iteration:
    for end in range(n):: We use a for loop with the end variable to iterate through the string. The end variable
    represents the ending index of our current sliding window.

Processing the Current Character:
    current_char = s[end]: In each iteration, we get the character at the current end index.

Checking for Repeating Characters:
    if current_char in char_index_map:: We check if the current_char is already present as a key in our char_index_map.
    If it is, it means we have encountered this character before within the string.
    start = max(start, char_index_map[current_char] + 1): This is the crucial part for handling repeating characters.
    char_index_map[current_char] gives us the index of the previous occurrence of current_char.
    char_index_map[current_char] + 1 is the index immediately after the previous occurrence. To maintain a substring
    without repeating characters, the start of our window must be after this previous occurrence.
    max(start, char_index_map[current_char] + 1): We take the maximum of the current start and the index after the
    previous occurrence. This is important because the previous occurrence might be before the current start of our
    window. In such a case, we don't need to move start. We only move start forward if the repeated character is within
    the current window.

Updating the Character's Last Seen Index:
    char_index_map[current_char] = end: We update the char_index_map with the current character and its current index
    (end). This ensures that char_index_map always stores the most recent index of each character encountered.

Updating the Maximum Length:
    max_len = max(max_len, end - start + 1): We calculate the length of the current substring without repeating characters,
    which is end - start + 1. We then update max_len if the current substring's length is greater than the current max_len.

Returning the Result:
    return max_len: After iterating through the entire string, max_len will hold the length of the longest substring
    without repeating characters, which we return.
"""


def longest_substring_without_repeating(s: str) -> int:
    n = len(s)
    max_len = 0
    start = 0
    char_index_map = {}
    for end in range(n):
        current_char = s[end]
        if current_char in char_index_map:
            start = max(start, char_index_map[current_char] + 1)
        char_index_map[current_char] = end
        max_len = max(max_len, end - start + 1)
    print(char_index_map)
    return max_len


str = input()
print(longest_substring_without_repeating(str))
