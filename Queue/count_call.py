class RoundQueue:
    def __init__(self):
        self.size = 10
        self.queue = [None for i in range(self.size)]
        self.front = 0
        self.rear = 0
    
    def is_queue_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def is_queue_empty(self):
        if self.rear == self.front:
            return True
        return False

    def en_queue(self, data):
        if RoundQueue.is_queue_full(self):
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        return

    def de_queue(self):
        if RoundQueue.is_queue_empty(self):
            return
        self.front = (self.front + 1) % self.size
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data

    def peek(self):
        return self.queue[(self.front + 1) % self.size]

    def time(self):
        time = 0
        for i in range(self.size):
            if self.queue[i] == None: continue
            time += self.queue[i][1]
        return time
    
if __name__ == '__main__':
    test_queue = RoundQueue()

    call_list = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3),('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3),('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4)]

    for i in range(len(call_list)):
        time = test_queue.time()

        if test_queue.is_queue_full():
            print("\n @2 상담이 종료되었습니다. @@")
            print(f"대기 시간 : {time}분")
            print(f"상담 대기 콜 : {test_queue.queue}")
            break

        print(f"대기 시간 : {time}분")
        print(f"상담 대기 콜 : {test_queue.queue}")
        test_queue.en_queue(call_list[i])