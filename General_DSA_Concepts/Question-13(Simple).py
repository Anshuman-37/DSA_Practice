#Question 13: Implement a singly Linked List

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

LinkedList = LinkedList()

LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)

print("This is the linked list",LinkedList.traverse())

LinkedList.delete_node(4)

print("This is the linked list",LinkedList.traverse())
