def m_sort(ary):
    if len(ary) == 1: return ary

    mid = len(ary) // 2
    left= m_sort(ary[:mid])
    right = m_sort(ary[mid:])
    m = merge(left, right)

    return m

def merge(left, right):
    l_p, r_p = 0, 0
    result = []

    while l_p < len(left) and r_p < len(right):
        if left[l_p] < right[r_p]:
            result.append(left[l_p])
            l_p += 1
        else:
            result.append(right[r_p])
            r_p += 1
    
    if l_p >= len(left): result += right[r_p:]
    else: result += left[l_p:]

    return result

lis = [1, 5, -2, 0, 3, 5, 2]
print(m_sort(lis))

