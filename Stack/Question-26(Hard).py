# Question 176: Reverse a stack using only stack operations (no recursion).
def reverse_stack_no_recursion(stack):
    if not stack:
        return

    aux_stack = []
    while stack:
        aux_stack.append(stack.pop())

    temp_stack = []
    while aux_stack:
        temp = aux_stack.pop()
        while stack:
            temp_stack.append(stack.pop())
        stack.append(temp)
        while temp_stack:
            stack.append(temp_stack.pop())

my_stack = [1, 2, 3, 4, 5]
print("Original Stack:", my_stack)

reverse_stack_no_recursion(my_stack)
print("Reversed Stack:", my_stack)