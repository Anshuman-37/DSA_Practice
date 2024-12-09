class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            print(f"Appended '{data}' as the head of the list.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Appended '{data}' to the list.")

    def create_cycle(self, pos):
        if pos == -1:
            print("No cycle created as pos is -1.")
            return
        cycle_start = None
        current = self.head
        index = 0
        last_node = None
        while current:
            if index == pos:
                cycle_start = current
                print(f"Cycle will start at node with data '{current.data}'.")
            last_node = current
            current = current.next
            index += 1
        if last_node and cycle_start:
            last_node.next = cycle_start
            print(
                f"Cycle created by connecting node with data '{last_node.data}' to node with data '{cycle_start.data}'.")

    def detect_cycle_floyd(self):
        slow = self.head
        fast = self.head
        step = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            step += 1
            print(f"Step {step}: Slow at '{slow.data}', Fast at '{fast.data if fast else 'None'}'")

            if slow == fast:
                print(f"Cycle detected at node with data '{slow.data}'.")
                return True
        print("No cycle detected in the list.")
        return False

    def display(self, limit=50):

        current = self.head
        count = 0
        nodes = []
        while current and count < limit:
            nodes.append(str(current.data))
            current = current.next
            count += 1
        if current:
            nodes.append("...")
        print("Linked List: " + " -> ".join(nodes))


if __name__ == "__main__":
    ll = LinkedList()

    for data in ['A', 'B', 'C', 'D', 'E']:
        ll.append(data)

    ll.display()

    print("\nDetecting cycle (expected: False):")
    has_cycle = ll.detect_cycle_floyd()
    print(f"Cycle detected: {has_cycle}")

    ll.create_cycle(pos=2)

    print("\nDetecting cycle after creating one (expected: True):")
    has_cycle = ll.detect_cycle_floyd()
    print(f"Cycle detected: {has_cycle}")

    print("\nDisplaying linked list with cycle (limited to 10 nodes):")
    ll.display(limit=10)
