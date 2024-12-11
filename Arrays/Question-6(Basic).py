# Question 6: Insert an element at a given index in an array.
def insert_with_check(lst, index, element):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < -len(lst) or index > len(lst):
        print(f"Index {index} is out of bounds")
        return
    lst.insert(index, element)
    print(f"Lst after insertion {lst}")


my_list = [1, 2, 3, 9, 10, 35]
insert_with_check(my_list, 10, 4)
insert_with_check(my_list, 4, 0)
