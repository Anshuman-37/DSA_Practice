# Question 8: Check for balanced parentheses using a stack.
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

string1 = "{[()]}"
string2 = "([)]"
print(f"{string1} is balanced: {is_balanced(string1)}")
print(f"{string2} is balanced: {is_balanced(string2)}")