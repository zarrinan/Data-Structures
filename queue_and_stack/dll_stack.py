import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#  add to tail, remove from tail -> array


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None

    def len(self):
        return self.size

# class Stack:
#     def __init__(self):
#         self.storage = DoublyLinkedList()

#     def push(self, value):
#         self.storage.add_to_tail(ListNode(value))

#     def pop(self):
#         return self.storage.remove_from_tail()

#     def len(self):
#         return self.storage.length