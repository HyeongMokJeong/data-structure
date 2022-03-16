from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드를 참조
    
class ChainHash: 
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시 테이블의 크기
        self. table = [None] * self.capacity
    
    def hash_value(self, key: Any) -> int: 
        # 키를 해시값으로 변환
        if isinstance(key, int): # 만약 key가 int형이 True 라면
            return key % self.capacity # key % capacity로 해시값 산출
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        # 정수(int)형이 아니라면, hashlib 모듈에서 제공하는 sha256 알고리즘을 사용하여 바이트 문자열의 해시값을 구함
        # hashlib.sha256에는 바이트 문자열의 인수를 전달해야하기 때문에, str(key)를 encode() 함수에 전달하여 바이트 문자열을 생성함
        # hexdigest() 함수는 sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냄
    
    def search(self, key: Any) -> Any:
        # 키가 key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key) # 검색하는 key의 해시값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 원소 추가
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None: # None이 나올 때까지
            if p.key == key: # p.key와 같은 key값이 있다면 이미 등록된 것이므로 False 반환
                return False
            p = p.next # 뒤쪽 노드를 차례차례 주목
        
        temp = Node(key, value, self.table[hash]) # None이 나올때까지 모든 노드를 주목했다면 입력받은 원소값을 Node로 만듬
        self.table[hash] = temp # 노드 추가
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash] # 노드를 주목
        pp = None # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else: 
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()