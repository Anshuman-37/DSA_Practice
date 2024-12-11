# Question 4: Reverse an array in-place.

lst = [1,2,3,4,5,6,7,8,9,10]

n = len(lst)

for i in range(0, n//2):
    lst[i], lst[n-i-1] = lst[n-i-1], lst[i]

print("Using manual approach")
print(lst)

# List comprehension solution for reversing an array in-place

print("Using in array slicing")
lst [:] = lst[::-1]
print(lst)