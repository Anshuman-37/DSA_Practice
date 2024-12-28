# Question 29:Find the longest substring with distinct characters in O(n).
def longest_substring_distinct_optimal(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    start = 0
    max_len = 0
    start_index = 0
    char_index_map = {}

    for end in range(n):
        current_char = s[end]
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1
        char_index_map[current_char] = end

        current_len = end - start + 1
        if current_len > max_len:
            max_len = current_len
            start_index = start

    return s[start_index : start_index + max_len]

s1 = "abcabcbb"
print(f"Optimal: {longest_substring_distinct_optimal(s1)}")

s2 = "bbbbb"
print(f"Optimal: {longest_substring_distinct_optimal(s2)}")

s3 = "pwwkew"
print(f"Optimal: {longest_substring_distinct_optimal(s3)}")

s4 = ""
print(f"Optimal: {longest_substring_distinct_optimal(s4)}")

s5 = "abcdefg"
print(f"Optimal: {longest_substring_distinct_optimal(s5)}")