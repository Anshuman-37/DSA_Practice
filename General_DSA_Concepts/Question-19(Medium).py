class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head  # Make it circular
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head  # Maintain circularity

    def traverse(self):
        if self.head is None:
            print("The list is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print()  # For a new line after traversal

    def remove(self, x):
        if self.head is None:
            print("The list is empty")
            return

        current = self.head
        previous = self.tail
        found = False

        while True:
            if current.data == x:
                found = True
                break
            previous = current
            current = current.next
            if current == self.head:
                break

        if not found:
            print(f"Element {x} not found in the list")
            return

        print(f"Removed {current.data}")

        # If the list has only one node
        if current == self.head and current == self.tail:
            self.head = self.tail = None
            return

        # If the node to be removed is the head
        if current == self.head:
            self.head = self.head.next
            self.tail.next = self.head
            return

        # If the node to be removed is the tail
        if current == self.tail:
            self.tail = previous
            self.tail.next = self.head
            return

        # Removing a node from the middle
        previous.next = current.next

# Example Usage
circular_list = CircularLinkedList()

for x in range(1, 6):
    circular_list.insert(x)

print("The circular linked list looks like:")
circular_list.traverse()

for x in range(1, 5):
    circular_list.remove(x)

print("The list after removal:")
circular_list.traverse()
