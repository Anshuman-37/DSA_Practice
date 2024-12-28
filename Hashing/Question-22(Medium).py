
"""
Explanation:
    We initialize max_len to 0, start of the window to 0, and a hash map char_counts to store the frequency of characters
    in the current window.
    We iterate through the string with the end pointer, expanding the window.
    For each character at the end pointer, we update its count in char_counts.
    If the number of distinct characters in the window (the size of char_counts) exceeds k, we shrink the window from
    the left by incrementing the start pointer.
    While shrinking the window, we decrement the count of the character at the start pointer in char_counts. If the
    count becomes 0, we remove the character from char_counts.
    In each iteration, we update max_len with the maximum window size encountered so far (which represents a valid substring).

Time Complexity: O(n)
    The end pointer iterates through the string once.
    The start pointer also moves at most n times.
    Hash map operations (insertion, deletion, lookup) take O(1) on average.

Space Complexity: O(k), in the worst case, the hash map will store k distinct characters.

Edge Cases:
    Empty string: The loop won't execute, and max_len will be 0.
    k = 0: The while loop condition will always be true if the window has any characters, so start will catch up to end,
     and max_len will remain 0.
    k >= number of unique characters in s: The while loop condition will never be met, and max_len will become the
    length of the string.
    String with all same characters: The while loop condition will never be met, and max_len will become the length of
    the string.
"""
def longest_substring_with_k_distinct_optimal(s: str, k: int) -> int:
    n = len(s)
    max_len = 0
    start = 0
    char_counts = {}
    for end in range(n):
        char_counts[s[end]] = char_counts.get(s[end], 0) + 1
        while len(char_counts) > k:
            char_counts[s[start]] -= 1
            if char_counts[s[start]] == 0:
                del char_counts[s[start]]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

s1 = "eceba"
k1 = 2
result1 = longest_substring_with_k_distinct_optimal(s1, k1)
print(f"String: '{s1}', k: {k1}, Longest Substring Length: {result1}")

s2 = "aaabbc"
k2 = 1
result2 = longest_substring_with_k_distinct_optimal(s2, k2)
print(f"String: '{s2}', k: {k2}, Longest Substring Length: {result2}")

