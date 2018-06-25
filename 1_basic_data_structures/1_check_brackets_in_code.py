#Uses python3
import sys

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def Push(self, item):
        self.items.append(item)
    def Pop(self):
        return self.items.pop()
    def Peek(self):
        return self.items[len(self.items)-1]
    def Size(self):
        return len(self.items)

def isbalanced(text):
    for i, next in enumerate(text.rstrip()):
        if next == '(' or next == '[' or next == '{':
            brackets_stack.Push((next,i))
        if next == ')' or next == ']' or next == '}':
            if brackets_stack.isEmpty():
                return i+1
            top = brackets_stack.Pop()
            if ((top[0] == '(' and next != ')') or
                (top[0] == '[' and next != ']') or
                (top[0] == '{' and next != '}')):
                return i+1
    if brackets_stack.isEmpty():
        return 'Success'
    else:
        return (brackets_stack.Peek()[1])+1

if __name__ == "__main__":
    text = sys.stdin.read()
    brackets_stack = Stack()
    print(isbalanced(text))


    # Printing answer, write your code here
