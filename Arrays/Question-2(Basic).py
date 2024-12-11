# Question 2: Find the largest and smallest element in an array.

lst = [6, 12, 1, 99, 999, 4, 7, 30, 0]

maxi = lst[0]
mini = lst[0]

for x in lst:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

print(f"Largest element: {maxi}")
print(f"Smallest element: {mini}")
