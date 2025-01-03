# Question 7: Reverse a string using a stack.
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

string = "hello"
reversed_string = reverse_string(string)
print(f"Original string: {string}")
print(f"Reversed string: {reversed_string}")