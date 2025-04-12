
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
    
    def print_linked_list(self):
        temp_node = self.head
        for _ in range(self.length):
            print(temp_node.value)
            temp_node = temp_node.next
        return True

my_linked_list = LinkedList(5)
print("Linked list initialization with a initial node: ")
my_linked_list.print_linked_list()

print("----------------------------")

print("After addding a new new node:")
my_linked_list.append(87)
my_linked_list.print_linked_list()