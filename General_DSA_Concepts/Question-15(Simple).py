# Question 15: Implement a Queue using a Linked List.
from dataclasses import dataclass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self,x):
        new_node = Node(x)
        if self.front is None:
            self.front = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.front is None:
            print("The queue is empty")
            return
        print(f"\nDe queueing element {self.front.data}",end="\n")
        self.front = self.front.next
        if self.front is None:
            self.tail = None

    def traverse_queue(self):
        if self.front is None:
            print("The queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end = "->")
            temp = temp.next

    def print_front(self):
        if self.front is None:
            print("The Queue is Empty")
        print(f"\nThe front is {self.front.data}")

    def print_rear(self):
        if self.tail is None:
            print("The queue is Empty")
        print(f"The rear is {self.tail.data}")


Queue = Queue()

Queue.enqueue(1), Queue.enqueue(2), Queue.enqueue(3), Queue.enqueue(4), Queue.enqueue(5)

print("The current queue looks like")
Queue.traverse_queue()

Queue.dequeue()
Queue.traverse_queue()
Queue.dequeue()

print("The current queue looks like")
Queue.traverse_queue()

Queue.print_front()
Queue.print_rear()
