# Question 15: Find an equilibrium index of an array.
def find_equilibrium_prefix_sum(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i # Equilibrium found
        left_sum += num
    return -1 # No equilibrium index found


arr = [-7, 1, 5, 2, -4, 3, 0]

print(f"Array:{arr}")
print(f"Result using prefix sum:{find_equilibrium_prefix_sum(arr)}")
