class Stack:
    def __init__(self):
        self.stack_list = []
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def reverse_string(value):
    stack = Stack()
    for s in value:
        stack.push(s)
    reverseString = ''
    for _ in range(len(stack.stack_list)):
        reverseString = reverseString + stack.pop()
    return reverseString

print(reverse_string('hello 11'))
        