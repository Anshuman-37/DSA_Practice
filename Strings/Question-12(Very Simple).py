# Question 12: Check if a string starts with another string (prefix check).

def starts_with_optimal(s: str, prefix: str) -> bool:
    return s.startswith(prefix)

print(starts_with_optimal("hello world", "hello"))
print(starts_with_optimal("hello world", "hell"))
print(starts_with_optimal("hello world", "o world"))
print(starts_with_optimal("hello world", "hello world!"))

