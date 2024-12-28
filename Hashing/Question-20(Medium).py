from collections import defaultdict

def four_sum_optimal(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    quadruplets = set()
    pair_sums = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            pair_sums[nums[i] + nums[j]].append((i, j))

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            remaining_sum = target - nums[i] - nums[j]
            if remaining_sum in pair_sums:
                for k_idx, l_idx in pair_sums[remaining_sum]:
                    if k_idx > j:
                        quadruplet = tuple(sorted((nums[i], nums[j], nums[k_idx], nums[l_idx])))
                        quadruplets.add(quadruplet)

    return [list(q) for q in quadruplets]

nums = [1, 0, -1, 0, -2, 2]
target = 0
result = four_sum_optimal(nums, target)
print(f"Input Array: {nums}")
print(f"Target Sum: {target}")
print(f"Four Sum Quadruplets: {result}")

nums2 = [2, 2, 2, 2, 2]
target2 = 8
result2 = four_sum_optimal(nums2, target2)
print(f"\nInput Array: {nums2}")
print(f"Target Sum: {target2}")
print(f"Four Sum Quadruplets: {result2}")

nums3 = [-3, -2, -1, 0, 0, 1, 2, 3]
target3 = 0
result3 = four_sum_optimal(nums3, target3)
print(f"\nInput Array: {nums3}")
print(f"Target Sum: {target3}")
print(f"Four Sum Quadruplets: {result3}")