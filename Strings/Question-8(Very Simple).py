# Question 8: Find the length of the longest word in a string.
def longest_word_length_split(s: str) -> int:
    words = s.split()
    if not words:
        return 0
    return max(len(word) for word in words)

print(longest_word_length_split("Find the length of the longest word"))