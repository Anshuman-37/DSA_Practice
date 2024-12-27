# Question 25: Find the minimum number of swaps to sort the array.
def min_swaps_optimal(nums):
    n = len(nums)
    arrpos = []
    for i in range(n):
        arrpos.append([nums[i], i])

    arrpos.sort()
    vis = [False] * n
    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][1]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


arr = [2, 8, 1, 5, 4, 10, 35]
print(min_swaps_optimal(arr))
