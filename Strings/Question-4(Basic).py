# Question 4: Count vowels and consonants in a string.

def count_vowels(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vow_count = 0
    length = len(s)
    for char in s:
        if char in vowels:
            vow_count += 1
    con_count = length - vow_count
    return vow_count, con_count

print(count_vowels("Anshuman"))

