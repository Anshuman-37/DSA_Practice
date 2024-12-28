# Question 10: Check if two strings are anagrams of each other.
def are_anagrams_optimal_hashmap(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    def get_char_counts(s):
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        return counts

    return get_char_counts(s1) == get_char_counts(s2)

print(are_anagrams_optimal_hashmap("listen", "silent"))
print(are_anagrams_optimal_hashmap("triangle", "integral"))
print(are_anagrams_optimal_hashmap("hello", "world"))