class Stack:
    def __init__(self) -> None:
        self.size = 10
        self.stack = [None for i in range(self.size)]
        self.top = -1

    def is_stack_full(self):
        if self.top >= self.size - 1:
            return True
        return False

    def is_stack_empty(self):
        if self.top == -1:
            return True
        return False
    
    def push(self, data):
        if Stack.is_stack_full(self):
            return
        self.top += 1
        self.stack[self.top] = data
        return

    def pop(self):
        if Stack.is_stack_empty(self):
            return
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if Stack.is_stack_empty(self):
            return
        return self.stack[self.top]

if __name__ == '__main__':
    test_stack = Stack()

    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>").lower()

        if select == 'i':
            print("입력할 데이터 ==>", end = ' ')
            data = input()
            test_stack.push(data)
            print(f"스택 상태 : {test_stack.stack}")
        elif select == 'e':
            data = test_stack.pop()
            print(f"추출된 데이터 : {data}")
            print(f"스택 상태 : {test_stack.stack}")
        elif select == 'v':
            print(f"확인된 데이터 : {test_stack.peek()}")
        elif select == 'x':
            break
        else:
            print("잘못된 입력")

    print("프로그램 종료!")