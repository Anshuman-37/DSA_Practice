# Question 28: Count distinct substrings using rolling hash (Rabin-Karp concept).
def count_distinct_substrings(s: str) -> int:
    n = len(s)
    distinct_hashes = set()
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            substring = s[i : i + length]
            hash_value = hash(substring)
            distinct_hashes.add(hash_value)
    return len(distinct_hashes)

s = "banana"
print(f"Rolling Hash (s1): {count_distinct_substrings(s)}")

s2 = "aaaa"
print(f"Rolling Hash (s2): {count_distinct_substrings(s2)}")

s3 = ""
print(f"Rolling Hash (s3): {count_distinct_substrings(s3)}")