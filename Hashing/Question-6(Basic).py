# Question 6: Count frequency of each character in a string using a hash map.

s = "Anshuman"

char_map = {}

for ch in s:
    char_map[ch] = char_map.get(ch, 0) + 1

print(char_map)
