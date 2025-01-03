# Question 9: Convert infix expression to postfix using a stack.
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

infix_expression = "A+B*C-D/E"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}")
