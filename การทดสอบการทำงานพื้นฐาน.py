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

def test_basic_operations():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack หลัง push: {stack.items}")
    print(f"ข้อมูลบนสุด: {stack.peek()}")
    print(f"ข้อมูลที่ pop: {stack.pop()}")
    print(f"Stack หลัง pop: {stack.items}")
    print(f"ขนาดของ Stack: {stack.size()}")