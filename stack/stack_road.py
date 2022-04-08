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

if __name__ == '__main__':
    test_stack = Stack()
    stoneAry = ['빨', '주', '노', '초', '파', '남', '보']

    print("과자집에 가는 길 : ", end = '')
    for i in stoneAry:
        test_stack.push(i)
        print(i, end = ' --> ')
    print("과자집")

    print("우리집에 가는 길 : ", end = '')
    for i in range(len(stoneAry)):
        print(f"{test_stack.pop()}", end = ' --> ')
    print("우리집")