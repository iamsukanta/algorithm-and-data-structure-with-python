# Singly Linked List Operation Implementations

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(4);
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1    
    
    def pop(self):
        if self.head is None:
            print('Linkedlist is empty')
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node.value
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return new_node.value

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1

    def get(self, index):
        if index >= self.length or index < 0 :
            return None;
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        prevNode = self.get(index - 1)
        currentNode = self.get(index)
        if currentNode:
            new_node = Node(value)
            new_node.next = currentNode
            if prevNode:
                prevNode.next = new_node
            else:
                currentNode = new_node
                self.head = currentNode
            self.length += 1
            return True
        else:
            if prevNode:
                new_node = Node(value)
                prevNode.next = new_node
                self.tail = new_node
                self.length += 1
                return True 
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            prevNode = self.get(index - 1)
            # Efficent way is
            currentNode = prevNode.next
            # currentNode = self.get(index)
            if prevNode:
                prevNode.next = currentNode.next
                currentNode.next = None
                self.length -= 1
            return prevNode
    
    def reverse(self):
        tempNode = self.head
        self.head = self.tail
        self.tail = tempNode
        after = tempNode.next
        before = None
        for _ in range(self.length):
            after = tempNode.next
            tempNode.next = before
            before = tempNode
            tempNode = after



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return 111

        

my_linked_list = LinkedList(4)
my_linked_list.append_node(17)
my_linked_list.append_node(13)
print('Before Pop: ')
my_linked_list.print_list()

my_linked_list.pop()
print('After Pop: ')
my_linked_list.print_list()

my_linked_list.prepend(44)
print('After Prepend: ')
my_linked_list.print_list()

my_linked_list.prepend(99)
print('After Prepend: ')
my_linked_list.print_list()

my_linked_list.pop_first()
print('After Pop First: ')
my_linked_list.print_list()

print('Get Node with index: ')
print(my_linked_list.get(2))

print('Set Node value  with index: ')
print(my_linked_list.set_value(5, 50))

print('After Set Node Value: ')
my_linked_list.print_list()

print('Insert new node in index: ')
my_linked_list.insert(5, 67)

print('Print LinkedList after adding new node at specific Index: ')
my_linked_list.print_list()

print('Delete node with index: 1')
my_linked_list.remove(1)

print('Print LinkedList after delete node at specific Index: ')
my_linked_list.print_list()

print('Again Insert new node in index: 2')
my_linked_list.insert(2, 90)

print('Print LinkedList after adding new node at specific Index: ')
my_linked_list.print_list()

print('Reverse the linked list: ')
my_linked_list.reverse()

print('Print the final linked list: ')
my_linked_list.print_list()

