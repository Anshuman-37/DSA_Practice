# Question 13: Implement strstr() to find a substring in a string.
def strstr_rabin_karp(haystack, needle):
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1

    d = 256
    q = 101

    m = len(needle)
    n = len(haystack)
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(needle[i])) % q
        t = (d * t + ord(haystack[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if haystack[i:i + m] == needle:
                return i

        if i < n - m:
            t = (d * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
            if t < 0:
                t = t + q
    return -1

haystack = "hello world"
needle = "world"

print(f"Rabin-Karp: {strstr_rabin_karp(haystack, needle)}")  # Output: 6

haystack = "this is a test string"
needle = "test"

print(f"Rabin-Karp: {strstr_rabin_karp(haystack, needle)}")  # Output: 10

haystack = "mississippi"
needle = "issip"

print(f"Rabin-Karp: {strstr_rabin_karp(haystack, needle)}")  # Output: 1