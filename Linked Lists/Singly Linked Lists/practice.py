
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            print("Linked List is Empty")
            return False
        
        if self.length is 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            for _ in range(self.length - 1):
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1
        return True
    
    def print_linked_list(self):
        temp_node = self.head
        if self.length:
            for _ in range(self.length):
                print(temp_node.value)
                temp_node = temp_node.next
        else:
            print("Linked List is Empty.")
        return True

my_linked_list = LinkedList(5)
print("Linked list initialization with a initial node: ")
my_linked_list.print_linked_list()

print("----------------------------")

print("After addding a new new node at the end:")
my_linked_list.append(87)
my_linked_list.print_linked_list()

print("After addding a new new node at the end:")
my_linked_list.append(11)
my_linked_list.print_linked_list()

print("After pop a new new node at the end:")
my_linked_list.pop()
my_linked_list.print_linked_list()

print("After pop a new new node at the end:")
my_linked_list.pop()
my_linked_list.print_linked_list()