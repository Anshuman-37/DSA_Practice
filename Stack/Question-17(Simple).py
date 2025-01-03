# Question 17: Delete the middle element in a stack
def delete_mid(stack, k):
    if not stack or k == 0:
        return

    temp = stack.pop()
    delete_mid(stack, k - 1)

    if k != len(stack) // 2 + 1:
        stack.append(temp)

stack = [1, 2, 3, 4, 5]
delete_mid(stack, len(stack))
print(f"Stack after deleting middle: {stack}")

stack = [1, 2, 3, 4, 5, 6]
delete_mid(stack, len(stack))
print(f"Stack after deleting middle: {stack}")