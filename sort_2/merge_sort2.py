def m_sort(ary):
    if len(ary) <= 1: return ary

    mid = len(ary) // 2
    left = m_sort(ary[:mid])
    right = m_sort(ary[mid:])
    result = merge(left, right)

    return result

def merge(left, right):
    lp, rp = 0, 0
    result = []

    while lp < len(left) and rp < len(right):
        if (left[lp] > right[rp]):
            result.append(right[rp])
            rp += 1
        else:
            result.append(left[lp])
            lp += 1
    
    if lp == len(left): result += right[rp:]
    else: result += left[lp:]

    return result

print(m_sort([1, -2, -5, 3, -2, 3, 9, 4]))