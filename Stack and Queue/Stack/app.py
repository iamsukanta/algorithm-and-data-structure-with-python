class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp


    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

print('Initialization stack with 4:')
my_stack = Stack(4)
my_stack.print_stack()

print('Stack item after 2 push:')
my_stack.push(5)
my_stack.push(58)
my_stack.print_stack()

print('Stack item after third pop:')
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_stack()