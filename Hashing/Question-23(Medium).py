def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mapping = {}
    for char_s, char_t in zip(s, t):
        if char_s not in mapping:
            mapping[char_s] = char_t
        elif mapping[char_s] != char_t:
            return False
    return True

s1 = "egg"
t1 = "add"
result1 = is_isomorphic(s1, t1)
print(f"String s: '{s1}', String t: '{t1}', Isomorphic: {result1}")

s2 = "foo"
t2 = "bar"
result2 = is_isomorphic(s2, t2)
print(f"String s: '{s2}', String t: '{t2}', Isomorphic: {result2}")

