# app/services/dsa_service.py
from collections import deque

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def to_list(self): return self.items

class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.popleft() if self.items else None
    def to_list(self): return list(self.items)

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
    def to_list(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

class HashTable:
    def __init__(self):
        self.table = {}
    def put(self, key, value): self.table[key] = value
    def get(self, key): return self.table.get(key)
    def delete(self, key): return self.table.pop(key, None)
    def to_dict(self): return self.table

# Singleton instances
stack = Stack()
queue = Queue()
linked_list = LinkedList()
hash_table = HashTable()