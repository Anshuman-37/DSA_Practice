class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = merge(left, right)
    return sorted_list

# Create a sample linked list: 4 -> 2 -> 1 -> 3
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

sorted_head = merge_sort_linked_list(head)

while sorted_head:
    print(sorted_head.data, end=" -> ")
    sorted_head = sorted_head.next
print("None") 