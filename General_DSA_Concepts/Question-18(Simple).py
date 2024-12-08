# Reverse a singly linked list iteratively and recursively.
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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

    def delete_node(self, key):
        current = self.head
        previous = None

        # Case 1: The list is empty
        if current is None:
            print("List is empty. Cannot delete.")
            return

        # Case 2: The node to be deleted is the head
        if current.data == key:
            self.head = current.next
            print(f"Deleted node with data {key} from the head.")
            return

        # Case 3: The node to be deleted is not the head
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key was not present in the list
        if current is None:
            print(f"Node with data {key} not found in the list.")
            return

        # Unlink the node from the list
        previous.next = current.next
        print(f"Deleted node with data {key} from the list.")

    def return_head(self):
        return self.head

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_recursive_helper(self, current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return self.reverse_recursive_helper(next_node, current)

    def reverse_recursive(self):
        self.head = self.reverse_recursive_helper(self.head, None)


linked_list = LinkedList()
linked_list.append(1), linked_list.append(2), linked_list.append(3), linked_list.append(4), linked_list.append(5)

linked_list.traverse()
linked_list.reverse_iterative()
print("\nAfter reversing")
linked_list.traverse()

print("\nAfter reversing again")
linked_list.reverse_recursive()
linked_list.traverse()
