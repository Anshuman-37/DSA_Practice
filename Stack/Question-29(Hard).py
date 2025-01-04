# Question 179: Implement a stack-based calculator for arithmetic expressions.
def evaluate_expression(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operand_stack = []
    operator_stack = []

    def apply_op():
        op = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        if op == '+':
            operand_stack.append(left + right)
        elif op == '-':
            operand_stack.append(left - right)
        elif op == '*':
            operand_stack.append(left * right)
        elif op == '/':
            operand_stack.append(left / right)

    for token in expression:
        if token.isdigit():
            operand_stack.append(int(token))
        elif token in precedence:
            while (operator_stack and
                   precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                apply_op()
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_op()
            operator_stack.pop()

    while operator_stack:
        apply_op()

    return operand_stack[0] if operand_stack else 0

expression = "2+3*4-5"
result = evaluate_expression(expression)
print(result)

expression = "(2+3)*(4-5)"
result = evaluate_expression(expression)
print(result)