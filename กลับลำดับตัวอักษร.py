class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

def reverse_string(input_str):
    stack_obj = Stack()
    for char in input_str:
        stack_obj.push(char)
    result = ""
    while not stack_obj.is_empty():
        result += stack_obj.pop()
    return result
text = input("ป้อนข้อความ: ")
print("ผลลัพธ์: ", reverse_string(text))