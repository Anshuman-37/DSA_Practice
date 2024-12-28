# Question 5: Reverse a string in place.

def rev_string_optimal(s):
    length = len(s)
    start = 0
    end = length-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s)

s = list("HEELOO")
print(rev_string_optimal(s))