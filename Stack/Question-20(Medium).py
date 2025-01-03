# Question 20: Find maximum area rectangle in a binary matrix using a stack.
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[i] <= heights[stack[-1]]:
            top_index = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            area = heights[top_index] * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area

def max_rectangle_area_in_binary_matrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == 1 else 0
        max_area = max(max_area, largest_rectangle_area(heights.copy()))

    return max_area

matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
result = max_rectangle_area_in_binary_matrix(matrix)
print(f"Binary matrix:\n{matrix}")
print(f"Largest rectangle area: {result}")