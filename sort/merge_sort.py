from pickle import NONE
from tkinter import N
from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    # 병합 정렬

    def _merge_sort(a:MutableSequence, left: int, right: int) -> None:
        # a[left] ~ a[right]를 재귀적으로 병합 정렬
        if left< right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center, right)
        
            p = j = 0
            i = k = left

            while i <= center: # 배열의 앞부분(a[left]~a[center]를 buff[0]~buff[center - left]로 복사)
                buff[p] = a[j]
                p += 1 # while문 종료 시 p값은 center - left + 1(인덱스 값 + 1)
                i += 1

            while i <= right and j < p: # 배열의 뒷부분(a[center + 1] ~ a[right])과 buff로 복사한 배열의 앞부분 p개를 병합하여 a에 저장
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p: # 배열 buff의 나머지 원소를 배열 a에 복사
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * N
    _merge_sort(a, 0, n - 1)