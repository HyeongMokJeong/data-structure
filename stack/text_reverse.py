class Stack:
    def __init__(self):
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
        return self.stack[self.top]


if __name__ =='__main__':
    test_stack = Stack()

    text = """진달래꽃\n나 보기가 역겨워\n가실 때에는\n말없이 고이 보내드리오리다.
    """
    print("----- 원본 -----")
    print(text)

    txt_list = text.split('\n')
    for i in range(len(txt_list)):
        test_stack.push(txt_list[i])

    print("----- 거꾸로 처리된 결과 -----")
    for i in range(len(txt_list)):
        print(test_stack.pop()[::-1])