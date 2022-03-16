from typing import Any

class FixedStack:
    # 고정 길이 스택 클래스

    class Empty(Exception):
        # 비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        # 가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity # 스택 크기
        self.ptr = 0 # 스택 포인터

    def __len__(self) -> int:
        # 스택에 쌓여있는 데이터 개수를 반환
        return self.ptr

    def is_empty(self) -> bool:
        # 스택이 비어있는지 판단
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        # 스택이 가득 차 있는지 판단
        return self.capacity <= self.ptr

    def push(self, value: Any) -> None:
        # 스택에 value를 푸시
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        # 꼭대기 데이터를 들여다봄
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        # stk에서 value를 찾아 인덱스를 반환
        for i in range(self.ptr -1, -1, -1): # self.ptr부터 0(-1 + 1)까지 역순으로 1씩
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> Any:
        # 스택에 value가 몇개 있는지 판단
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])