# Question 27: Word Pattern problem (string follows a given pattern) using a hash map.
def word_pattern_optimal(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    pattern_to_word = {}
    word_to_pattern = {}

    for p_char, word in zip(pattern, words):
        if p_char not in pattern_to_word:
            if word in word_to_pattern:
                return False
            pattern_to_word[p_char] = word
            word_to_pattern[word] = p_char
        elif pattern_to_word[p_char] != word:
            return False

    return True

print(f"word_pattern_optimal('abba', 'dog cat cat dog'): {word_pattern_optimal('abba', 'dog cat cat dog')}")  # True
print(f"word_pattern_optimal('abba', 'dog cat cat fish'): {word_pattern_optimal('abba', 'dog cat cat fish')}") # False
print(f"word_pattern_optimal('aaaa', 'dog cat cat dog'): {word_pattern_optimal('aaaa', 'dog cat cat dog')}") # False
print(f"word_pattern_optimal('abba', 'dog dog dog dog'): {word_pattern_optimal('abba', 'dog dog dog dog')}") # False
print(f"word_pattern_optimal('', ''): {word_pattern_optimal('', '')}") # True
print(f"word_pattern_optimal('a', 'b'): {word_pattern_optimal('a', 'b')}") # True
print(f"word_pattern_optimal('aa', 'dog dog'): {word_pattern_optimal('aa', 'dog dog')}") # True
print(f"word_pattern_optimal('ab', 'dog dog'): {word_pattern_optimal('ab', 'dog dog')}") # False
