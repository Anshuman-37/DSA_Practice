# Question 12: Sort a stack using recursion.
def sorted_insert(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
        return
    temp = stack.pop()
    sorted_insert(stack, element)
    stack.append(temp)

def sort_stack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    sort_stack(stack)
    sorted_insert(stack, temp)

# Example usage
stack = [3, 1, 4, 2]
sort_stack(stack)
print(f"Sorted stack: {stack}")