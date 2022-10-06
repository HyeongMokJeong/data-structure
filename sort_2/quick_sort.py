def q_sort(ary, start, end):
    if (start < end): 
        p = getpivot(ary, start, end)
        q_sort(ary, start, p - 1)
        q_sort(ary, p, end)

    return ary

def getpivot(ary, start, end):
    s = start - 1

    for i in range(start, end):
        if (ary[i] <= ary[end]):
            s += 1
            ary[s], ary[i] = ary[i], ary[s]
    ary[s + 1], ary[end] = ary[end], ary[s + 1]

    return s + 1

lis = [1, 6, -2, 3, 4, -5]
print(q_sort(lis, 0, len(lis) - 1))