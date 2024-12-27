# Question 11: Check if one string is a permutation of another using frequency count.

from collections import Counter

def are_permutations(str1, str2):
    if len(str1) != len(str2):
        return False

    freq_map1 = Counter(str1)
    freq_map2 = Counter(str2)

    return freq_map1 == freq_map2

string1 = "listen"
string2 = "silent"
print(are_permutations(string1, string2))

string3 = "hello"
string4 = "world"
print(are_permutations(string3, string4))

string5 = "aab"
string6 = "aba"
print(are_permutations(string5, string6))

string7 = "aab"
string8 = "abb"
print(are_permutations(string7, string8))