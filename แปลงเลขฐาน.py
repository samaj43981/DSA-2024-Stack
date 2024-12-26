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