class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length is 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length is 0:
            return None
        temp = self.tail
        if self.length is 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length is 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length is 0:
            return None
        temp = self.head
        if self.length is 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < (self.length/2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if self.length == index:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.next

my_doubly_linked_list = DoublyLinkedLists(4)
my_doubly_linked_list.print_list()

print('----------------- After append new node at the end:------------------')
my_doubly_linked_list.append(25)
my_doubly_linked_list.print_list()

print('----------------- After append new node at the end:------------------')
my_doubly_linked_list.append(99)
my_doubly_linked_list.print_list()

print('----------------- After pop at the end:------------------')
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()

print('----------------- After prepend node at the beginning:------------------')
my_doubly_linked_list.prepend(89)
my_doubly_linked_list.print_list()

print('----------------- After pop first at the beginning:------------------')
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()

print('----------------- Get node with specific index ------------------')
print(my_doubly_linked_list.get(0))

print('----------------- Set node with specific index ------------------')
my_doubly_linked_list.set_value(0, 57)
my_doubly_linked_list.print_list()

print('----------------- Insert node with specific index ------------------')
my_doubly_linked_list.insert(2, 90)
my_doubly_linked_list.print_list()