from __future__ import annotations
from pstats import Stats
from traceback import StackSummary # 파이썬 구버전에서도 신버전의 기능을 사용할 수 있게 해줌
from typing import Any, Type
from enum import Enum
import hashlib

from cv2 import FlannBasedMatcher

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 # 데이터를 저장
    EMPTY = 1 # 비어 있음
    DELETED = 2 # 삭제 완료

class Bucket:
    # 해시를 구성하는 버킷
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        # 모든 필드에 값을 설정
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat: Status) -> None:
        # 속성을 설정
        self.stat = stat

class OpenHash:
    # 오픈 주소법으로 구현하는 해시 클래스
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        # 해시값을 구함
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        # 재해시값을 구함
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break

            elif p.stat == Status.OCCUPIED and p.key == key:
                return p

            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.DELETED:
                print('---삭제 완료---')
            elif self.table[i].stat == Status.EMPTY:
                print('---미등록---')