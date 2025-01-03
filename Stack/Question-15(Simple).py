# Question 15: Reverse a stack using recursion (no extra stack).
def reverse_stack_recursive(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack_recursive(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)

my_stack = [1, 2, 3, 4, 5]
print("Original Stack:", my_stack)
reverse_stack_recursive(my_stack)
print("Reversed Stack:", my_stack)