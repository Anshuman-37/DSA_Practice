# Question 13: Find the first non-repeating character in a string using a hash map.
from collections import Counter


def first_non_repeating_character(string):
    if not string:
        return -1

    if len(string) == 1:
        return string

    map = Counter(string)
    for char in string:
        if map[char] == 1:
            return char

    return -1


str = "eeleetcode"
print(first_non_repeating_character(str))

