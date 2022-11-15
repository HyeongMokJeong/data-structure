A = [16, 8, 15, 5, 7, 13, 14, 2, 4]

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

def h_sort(ary):
    result = []
    for end in range(len(ary) - 1, 0, -1):
        m_h(ary, 0)
        ary[0], ary[end] = ary[end], ary[0]
        result.append(ary[end])
        ary = ary[:end]
    return result

result = h_sort(A)
print(result)