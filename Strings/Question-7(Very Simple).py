# Question 7: Check if two strings are rotations of each other.

def are_rotations_optimal(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or not s1:
        return False
    return s2 in s1 + s1

print(are_rotations_optimal("waterbottle", "erbottlewat"))
print(are_rotations_optimal("waterbottle", "bottlewater"))
print(are_rotations_optimal("waterbottle", "elttobretaw"))
print(are_rotations_optimal("abc", "bca"))
print(are_rotations_optimal("abc", "cab"))
print(are_rotations_optimal("abc", "acb"))

