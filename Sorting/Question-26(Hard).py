# Question 26: Group and sort words by their anagram classes.

from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_groups[sorted_word].append(word)

    for group in anagram_groups.values():
        group.sort()

    return list(anagram_groups.values())

