# Question 9: Move all zeros to the end of the array.


def move_zeros_to_end(lst):
    if not lst:
        print("List is empty")
        return lst
    start=0
    end = len(lst)-1
    while start < end:
        if lst[start]==0:
            lst[start] , lst[end] = lst[end], lst[start]
            end -= 1
        else:
            start += 1
    return lst

def move_zeros_preserve_order(lst):
    if not lst:
        print("List is empty")
        return lst
    write_index = 0
    for read_index in range(len(lst)):
        if lst[read_index] != 0:
            lst[write_index] = lst[read_index]
            write_index += 1
    for i in range(write_index, len(lst)):
        lst[i] = 0
    return lst

lst = [1,0,4,2,4,0,5,0,6,0,7,0,8,0,9,0,10]
print(f"Before moving zeros to the end: {lst}")
print(f"After moving zeros to the end: {move_zeros_to_end(lst)}")
