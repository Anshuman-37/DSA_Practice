# Question 21: Container With Most Water
def max_area(height):
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area_result = max_area(height)
print(f"The maximum area of water is: {max_area_result}")