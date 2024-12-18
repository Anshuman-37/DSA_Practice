# Question 28: Trapping Rain Water problem.
"""
Explanation:
    We use two pointers, left and right, starting from the beginning and end of the height array respectively.
    max_left and max_right track the maximum heights seen so far from the left and right.
    In each iteration, we process the shorter bar (height[left] or height[right]). If the current bar is taller than or equal to the maximum seen so far from its side, we update the maximum. Otherwise, we add trapped water.
    We move the pointer of the shorter bar inward.
Time Complexity: O(n). We traverse the height array once.
Space Complexity: O(1). We use only constant extra space.
Edge Cases: Handles empty input and single/double bar cases correctly.
"""
def trap_two_pointers(height):
    n = len(height)
    if n == 0:  return 0

    left = 0
    right = n - 1
    max_left = 0
    max_right = 0
    total_water = 0

    while left < right:
        if height[left] <= height[right]:  # Process the shorter bar
            if height[left] >= max_left:  # Update max_left
                max_left = height[left]
            else:
                total_water += max_left - height[left]  # Add trapped water
            left += 1
        else:
            if height[right] >= max_right:  # Update max_right
                max_right = height[right]
            else:
                total_water += max_right - height[right]  # Add trapped water
            right -= 1

    return total_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_two_pointers(height))