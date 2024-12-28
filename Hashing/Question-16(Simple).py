# Question 16: Find duplicates within k distance in an array.
def find_duplicates_within_k_optimal(nums: list[int], k: int) -> bool:
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if i >= k:
            seen.remove(nums[i - k])
    return False

arr = [1,4,5,6,1,4,0,2,19]
print(find_duplicates_within_k_optimal(arr, 5))
