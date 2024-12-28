# Question 15: Group anagrams using hashing.
from collections import defaultdict

def group_anagrams_optimal(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        anagram_map[tuple(count)].append(s)
    return list(anagram_map.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

grouped_anagrams = group_anagrams_optimal(input_strings)

# Print the output
print("Input strings:", input_strings)
print("Grouped anagrams:", grouped_anagrams)
