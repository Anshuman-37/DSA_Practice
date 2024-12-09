# Question 20: Implement a Deque (double-ended queue) and show all operations.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, x):
        """Insert an element at the front of the deque."""
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_back(self, x):
        """Insert an element at the back of the deque."""
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def traverse_front(self):
        """Traverse and print the list from front to back."""
        if self.head is None:
            print("The deque is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data}", end=" <-> ")
            temp = temp.next
        print("None")

    def traverse_back(self):
        """Traverse and print the list from back to front."""
        if self.tail is None:
            print("The deque is empty")
            return
        temp = self.tail
        while temp:
            print(f"{temp.data}", end=" <-> ")
            temp = temp.prev
        print("None")

    def delete_front(self):
        if self.head is None:
            print("The deque is empty")
            return
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print(f"Deleted {removed_data} from the front")

    def delete_back(self):
        if self.tail is None:
            print("The deque is empty")
            return
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print(f"Deleted {removed_data} from the back")

    def delete_value(self, x):
        if self.head is None:
            print("The deque is empty")
            return

        # If the node to be deleted is the head
        if self.head.data == x:
            self.delete_front()
            return

        # If the node to be deleted is the tail
        if self.tail.data == x:
            self.delete_back()
            return

        # Traverse to find the node to delete
        current = self.head.next
        while current and current.data != x:
            current = current.next

        if current is None:
            print(f"Value {x} not found in the deque")
            return

        # Adjust the pointers
        current.prev.next = current.next
        current.next.prev = current.prev
        print(f"Deleted {x} from the deque")


# Example Usage:

deque = DoublyLinkedList()

for x in range(1, 6):
    deque.insert_back(x)

print("Deque after inserting at the back:")
deque.traverse_front()

for x in range(6, 9):
    deque.insert_front(x)

print("\nDeque after inserting at the front:")
deque.traverse_front()

print("\nTraversing the deque from back to front:")
deque.traverse_back()

for x in [2, 5, 7]:
    deque.delete_value(x)

print("\nDeque after deletions:")
deque.traverse_front()

deque.delete_front()
deque.delete_back()

print("\nDeque after deleting from front and back:")
deque.traverse_front()


