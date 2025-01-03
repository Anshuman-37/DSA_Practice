# Question 10: Evaluate a postfix expression using a stack.
def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if char == '+':
                stack.append(val1 + val2)
            elif char == '-':
                stack.append(val1 - val2)
            elif char == '*':
                stack.append(val1 * val2)
            elif char == '/':
                stack.append(val1 / val2)
    return stack.pop()

# Example usage
postfix_expression = "231*+9-"
result = evaluate_postfix(postfix_expression)
print(f"Postfix expression: {postfix_expression}")
print(f"Result: {result}")