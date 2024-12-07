#Question 11: Convert an array of elements into a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the head of the list.")
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print(f"Inserted {data} at the end of the list.")

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def to_linked_list(self, array):
        for element in array:
            self.append(element)

    def to_list(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

array = [10, 20, 30, 40, 50]
linked_list = LinkedList()

print("Converting array to linked list:")
linked_list.to_linked_list(array)

print("\nTraversing the linked list:")
linked_list.traverse()

converted_array = linked_list.to_list()
print("\nConverted linked list back to array:")
print(converted_array)