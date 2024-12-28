# Question 14: Smallest window in a string containing all characters of another string.
def smallest_window_optimal(s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    if not t or not s:
        return ""

    if m > n:
        return ""

    t_counts = {}
    for char in t:
        t_counts[char] = t_counts.get(char, 0) + 1

    required_chars = len(t_counts)
    formed_chars = 0
    window_counts = {}
    min_len = float('inf')
    result = ""
    left = 0

    for right in range(n):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_counts and window_counts[char] == t_counts[char]:
            formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left : right + 1]

            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in t_counts and window_counts[left_char] < t_counts[left_char]:
                formed_chars -= 1
            left += 1

    return result


s2 = "AA"
t2 = "AA"
optimal_result_2 = smallest_window_optimal(s2, t2)
print(f"Optimal Result for s='AA', t='AA': {optimal_result_2}")

s3 = "ADOBECODEBANC"
t3 = "AAAC"
optimal_result_3 = smallest_window_optimal(s3, t3)
print(f"Optimal Result for s='ADOBECODEBANC', t='AAAC': {optimal_result_3}")

s4 = "a"
t4 = "aa"
optimal_result_4 = smallest_window_optimal(s4, t4)
print(f"Optimal Result for s='a', t='aa': {optimal_result_4}")

s5 = "abc"
t5 = ""
optimal_result_5 = smallest_window_optimal(s5, t5)
print(f"Optimal Result for s='abc', t='': {optimal_result_5}")

s6 = ""
t6 = "abc"
optimal_result_6 = smallest_window_optimal(s6, t6)
print(f"Optimal Result for s='', t='abc': {optimal_result_6}")