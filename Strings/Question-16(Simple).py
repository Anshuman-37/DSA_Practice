# Question 16: Check if two strings differ by exactly one character
def differ_by_one_optimized(str1, str2):
    if len(str1) != len(str2):
        return False

    diff_count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

str1 = "pale"
str2 = "ple"

print(f"Optimized: {differ_by_one_optimized(str1, str2)}")  # Output: False

str1 = "pales"
str2 = "pale"

print(f"Optimized: {differ_by_one_optimized(str1, str2)}")  # Output: False

str1 = "pale"
str2 = "bale"

print(f"Optimized: {differ_by_one_optimized(str1, str2)}")  # Output: True