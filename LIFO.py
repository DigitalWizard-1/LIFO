class Stack:
    def __init__(self, stk):
        self.stack = stk

    def isempty(self) -> bool:
        if self.stack:
            return True
        else:
            return False

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':

    example = Stack([])
    text = '[([])((([[[]]])))]{()}'  # подаем текст на вход
    print('Строка на вход:', text)

    for id in text:
        if not example.isempty():
            example.push(id)
        elif id == ')' and example.peek() == '(':
            example.pop()
        elif id == '}' and example.peek() == '{':
            example.pop()
        elif id == ']' and example.peek() == '[':
            example.pop()
        else:
            example.push(id)

    if example.isempty():
        print('Несбалансировано')
    else:
        print('Сбалансировано')
