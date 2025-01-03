# Question 18: Next greater element using a stack
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

arr = [4, 5, 2, 25]
result = next_greater_element(arr)
print(f"Input array: {arr}")
print(f"Next greater elements: {result}")