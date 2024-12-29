# Question 14:  Check if a string is a valid shuffle of two other strings.
from collections import Counter

def is_valid_shuffle_hashmap(str1, str2, shuffle):
    if len(shuffle) != len(str1) + len(str2):
        return False

    char_counts = Counter(str1 + str2)

    for char in shuffle:
        if char in char_counts and char_counts[char] > 0:
            char_counts[char] -= 1
        else:
            return False

    return all(count == 0 for count in char_counts.values())

str1 = "abc"
str2 = "def"
shuffle = "dabecf"

print(is_valid_shuffle_hashmap(str1, str2, shuffle))

str1 = "xy"
str2 = "12"
shuffle = "x1y2"

print(is_valid_shuffle_hashmap(str1, str2, shuffle))

str1 = "chocolate"
str2 = "chips"
shuffle = "cchocohilaptes"

print(is_valid_shuffle_hashmap(str1, str2, shuffle))