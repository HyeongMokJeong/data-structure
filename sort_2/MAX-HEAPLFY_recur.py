A = [4, 16, 15, 8, 7, 13, 14, 2, 5]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def m_h(ary, idx):
    left = idx * 2 + 1
    right = idx * 2 + 2

    big = idx
    if (left < len(ary) and ary[big] < ary[left]):
        big = left
    if (right < len(ary) and ary[big] < ary[right]):
        big = right
    if (big != idx):
        ary[big], ary[idx] = ary[idx], ary[big]
        m_h(ary, big)

for i in range(len(A)):
    m_h(A, i)

print(A)