class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [ None for _ in range(self.size) ]
        self.top = -1

    def is_stack_full(self):
        if self.top == self.size - 1:
            return True
        return False

    def is_stack_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        if Stack.is_stack_full(self):
            return
        self. top += 1
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

    def validate_stack_sequences(self, pushed, popped):
        # 리스트로 구현
        # push_list = []
        # pop_list = []
        # count = 0

        # for i in range(len(pushed)):
        #     if pushed[i] == popped[count]:
        #         pop_list.append(pushed[i])
        #         count += 1
        #     else:
        #         push_list.append(pushed[i])
        
        # for i in range(len(push_list) - 1, -1, -1):
        #     pop_list.append(push_list[i])
        
        # print(pop_list)
        # if pop_list == popped: return True
        # else: return False
        stack_push = Stack() 
        stack_pop = Stack() 
        count = 0 
        same = 0

        for i in range(len(pushed)):
            stack_push.push(pushed[i]) 
            if pushed[i] == popped[count]: 
                stack_pop.push(stack_push.pop()) 
                count += 1 

        while stack_push.top != -1: 
            stack_pop.push(stack_push.pop()) 
        
        for i in range(len(popped)): 
            if stack_pop.stack[i] == popped[i]: same += 1 
        if same == len(popped): return True 
        else: return False


if __name__ == '__main__':
    test_stack = Stack()
    pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    popped = [[3, 4, 5, 2, 1], [4, 5, 2, 3, 1]]
    for i in range(len(pushed)):
        print(test_stack.validate_stack_sequences(pushed[i], popped[i]))