# Question 26: KMP algorithm for pattern searching (implement and explain).
def compute_lps_array(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = compute_lps_array(pattern)
    j = 0

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]


        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

kmp_search(text, pattern)
