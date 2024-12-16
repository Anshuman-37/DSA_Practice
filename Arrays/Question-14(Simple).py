# Question 44: Find the missing number in an array of size n containing elements from 1 to n.
def find_missing_number_xor(arr , n):
    xor_all = 0
    for nums in arr:
        xor_all ^= nums
    for n in range(0,n+1):
        xor_all ^= n
    return xor_all

def find_missing_number(arr, n):
    sum_all = 0
    for nums in arr:
        sum_all += nums
    sum_n = n*(n+1)//2
    return sum_n - sum_all

arr = [1,2,3,4,6,7,8,9,10,11]
n = 11

print(f"Array: {arr}")
print(f"The missing number is {find_missing_number_xor(arr,n)}")

print(f"Array: {arr}")
print(f"The missing number is {find_missing_number(arr,n)}")