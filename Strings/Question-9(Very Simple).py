# Question 9: Count occurrences of a substring in a string.
def count_substring_kmp(text: str, sub: str) -> int:
    n = len(text)
    m = len(sub)
    if m == 0:
        return 0  # Or handle as an error

    count = 0
    # Compute the Longest Proper Prefix Suffix (LPS) array
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1
    while i < m:
        if sub[i] == sub[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Search for the substring
    i = 0  # index for text[]
    j = 0  # index for sub[]
    while i < n:
        if text[i] == sub[j]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j - 1]  # Prepare for the next possible occurrence (overlapping)
        elif i < n and text[i] != sub[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count

print(count_substring_kmp("This is a test string is", "is"))