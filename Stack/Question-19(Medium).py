# Question 19: Largest rectangle in a histogram using a stack.
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

heights = [2, 1, 5, 6, 2, 3]
result = largest_rectangle_area(heights)
print(f"Histogram: {heights}")
print(f"Largest rectangle area: {result}")