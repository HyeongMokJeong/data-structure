from typing import MutableSequence

def shaker_sort(a: MutableSequence):
    left = 0
    right = len(a) - 1
    last = right

    while left < right:
        for i in range(right, left, -1): # 오른쪽에서 왼쪽으로
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1] # 작은 원소를 앞으로 이동시킴
                last = i
        left = last

        for j in range(left, right): # 왼쪽에서 오른쪽으로
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last