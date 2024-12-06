### Linked List

A linked list is a fundamental data structure in computer science used to organize items sequentially. Unlike arrays,
linked lists consist of nodes where each node contains data and a reference (or pointer) to the next node in the
sequence. This structure allows for efficient insertion and deletion of elements.

#### Types of Linked Lists

* _Singly Linked List_:
  Each node points to the next node.
  Traversal is unidirectional (from head to tail).

* _Doubly Linked List_:
  Each node points to both the next and the previous node.
  Allows bidirectional traversal.

* _Circular Linked List_:
  The last node points back to the first node.
  Can be singly or doubly linked.

#### Characteristics of a Singly Linked List

* Dynamic Size: Can easily grow or shrink by adding or removing nodes.
* Ease of Insertion/Deletion: Particularly efficient for operations at the beginning of the list.
* Sequential Access: Accessing elements requires traversing from the head node.
* No Random Access: Unlike arrays, direct access to an element by index is not possible.

#### Structure of a Singly Linked List

Each node in a singly linked list typically contains:

* Data: The value or information stored in the node.
* Next Pointer: A reference to the next node in the list.
  Node Representation:

```css

[ Data | Next ] -> [ Data | Next ] -> [ Data | Next ] -> None
```

* Head: The first node in the linked list.
* Tail: The last node, which points to None.

#### Inserting an Element at the End of a Singly Linked List
```css

Initial List:
Head -> [ A | Next ] -> [ B | Next ] -> [ C | Next ] -> None

After Inserting D:
Head -> [ A | Next ] -> [ B | Next ] -> [ C | Next ] -> [ D | Next ] -> None
```

#### Python Implementation
*_Class Node_*
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
```

*_SinglyLinkedList Class_*
```python

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert_at_end(self, data):
        """
        Insert a new node with the specified data at the end of the list.
        """
        new_node = Node(data)  # Step 1: Create a new node
        if self.head is None:
            # Step 2a: If the list is empty, set new node as head
            self.head = new_node
            print(f"Inserted {data} as the head of the list.")
            return
        # Step 2b: Traverse to the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # Step 3: Update the next pointer
        print(f"Inserted {data} at the end of the list.")

    def display(self):
        """
        Display the linked list.
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

```