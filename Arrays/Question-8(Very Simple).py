# Question 8: Rotate an array by k steps.

def rotate_array(lst: list, k: int):
    if not lst:
        print("Empty list")
        return lst
    n = len(lst)
    k = k % n
    lst[:] = lst[-k:] + lst[:-k]
    return lst


## Without extra space
def rotate_array_reversal(lst: list, k: int):
    if not lst:
        print("Empty list")
        return lst
    n = len(lst)
    k = k % n

    def reverse(sub_lst, start, end):
        while start < end:
            sub_lst[start], sub_lst[end] = sub_lst[end], sub_lst[start]
            start += 1
            end -= 1

    reverse(lst, 0, n - 1)
    reverse(lst, 0, k - 1)
    reverse(lst, k, n - 1)
    return lst


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4
print(f"Before rotation: {lst}")
print(f"After rotating {k} steps: {rotate_array_reversal(lst, k)}")
