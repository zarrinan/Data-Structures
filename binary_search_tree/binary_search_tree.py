import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # if there is no self.left value
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                sub_tree_contains = self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)

        return sub_tree_contains

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        # recursive solution

        # if we can go right, go right
        # return when we can't go right anymore
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # iterative solution
        current_tree_root = self
        while current_tree_root.right:
            current_tree_root = current_tree_root.right

        return current_tree_root.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print the current node
        # go left if you can
        # go right if you can
        print(node.value)
        if node.left:
            self.in_order_print(node.left)
            
        elif node.right:
            self.in_order_print(node.right)
            # print(node.value)
       
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue to keep track of nodes
        # place the first node onto queue

        # while queue isnt empty:
        # deque the top node
        # print the node
        # add children to the queue
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            current_node = q.dequeue().value
            print(current_node.value)

            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack to keep track of nodes
        # place the first node onto stack

        # while stack isnt empty:
        # pop the top node
        # print the node
        # add children to the stack
        # remember which children to add first,
        # because that changes the output order

        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        
        if node.right:
            self.post_order_dft(node.right)
        
        print(node.value)
