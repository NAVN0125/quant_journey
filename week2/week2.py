# Tasks/Objectives:
# The "Undo" Stack: Create a class-based Stack that mimics a browser's "back" button logic.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


# Manual Linked List: Build a Node class and a LinkedList class. Write a function to reverse the list without using .reverse().

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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = current

    def print_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

obj = LinkedList()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
print(obj.print_list())
obj.reverse()
print(obj.print_list())

# The Big O Table: Create a markdown file in your GitHub repo mapping 5 common Python functions (like .append() vs .insert(0, x)) to their Big O complexities.