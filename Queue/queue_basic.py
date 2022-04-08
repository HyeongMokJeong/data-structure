class Queue:
    def __init__(self) -> None:
        self.size = 10
        self.queue = [None for i in range(self.size)]
        self.front = -1
        self.rear = -1
    
    def is_queue_full(self):
        if self.rear >= self.size - 1:
            if self.front != -1:
                for i in range(self.front + 1, self.size):
                    self.queue[i - 1] = self.queue[i]
                    self.queue[i] = None
                return False
            return True
        return False
    
    def is_queue_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def en_queue(self, data):
        if Queue.is_queue_full(self):
            return
        self.rear += 1
        self.queue[self.rear] = data
        return

    def de_queue(self):
        if Queue.is_queue_empty(self):
            return
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data

    def peek(self):
        if Queue.is_queue_empty(self):
            return
        return self.queue[self.front + 1]

if __name__ == '__main__':
    test_queue = Queue()

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> ').lower()

        if select == 'i':
            data = input("삽입할 데이터 --> ")
            test_queue.en_queue(data)
            print(f"큐 상태 : {test_queue.queue}")
        
        elif select == 'v':
            print(f"확인된 데이터 --> {test_queue.peek()}")
        
        elif select == 'e':
            print(f"추출된 데이터 --> {test_queue.de_queue()}")
            print(f"큐 상태 : {test_queue.queue}")

        elif select == 'x':
            break
        
        else:
            print('잘못된 입력')
    
    print("프로그램 종료!")