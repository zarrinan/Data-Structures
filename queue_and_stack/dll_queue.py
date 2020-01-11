import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

# add to tail remove from head -> DLL


class Queue:
    def __init__(self):
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        return self.storage.add_to_tail(ListNode(value))

    def dequeue(self):
        return self.storage.remove_from_head()
        
    def len(self):
        return self.storage.length


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def enqueue(self, item):
#         self.size += 1
#         self.storage.append(item)
    
#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         return None

#     def len(self):
#         return self.size
