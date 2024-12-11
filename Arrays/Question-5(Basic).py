# Question 5: Check if an array is sorted.

lst = [1,2,3,4,5,6,7,8,9,10]

is_sorted = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(f"Is the array sorted? {is_sorted}")
