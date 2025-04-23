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

def is_balanced_parentheses(value):
    stack = Stack()

    for s in value:
        if s == '(':
            stack.push(s)
        elif s == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()



print(is_balanced_parentheses('(())))'))

print(is_balanced_parentheses('(())'))