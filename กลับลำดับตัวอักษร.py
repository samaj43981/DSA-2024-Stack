def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result

text = input("ป้อนข้อความ: ")
print("ผลลัพธ์: ", reverse_string(text))