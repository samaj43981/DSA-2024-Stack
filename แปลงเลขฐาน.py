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

def base_conversion(num, base):
    stack = Stack()
    digits = "0123456789ABCDEF"
    while num > 0:
        stack.push(digits[num % base])
        num //= base
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result

num = int(input("ป้อนตัวเลขฐาน 10: "))
print("ฐาน 2: ", base_conversion(num, 2))
print("ฐาน 16: ", base_conversion(num, 16))