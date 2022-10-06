def s_sort(ary):
    for end in range(len(ary) - 1, 0, -1):
        big = end
        for i in range(0, end):
            if ary[i] > ary[big]:
                big = i
        ary[end], ary[big] = ary[big], ary[end]
    return ary

def b_sort(ary):
    for i in range(len(ary) - 1):
        for j in range(i + 1, len(ary)):
            if ary[i] > ary[j]:
                ary[i], ary[j] = ary[j], ary[i]
    return ary

def i_sort(ary):
    for i in range(1, len(ary)):
        for j in range(i, 0, -1):
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
    return ary


print(i_sort([1, 4, 3, 9, 2, -2]))