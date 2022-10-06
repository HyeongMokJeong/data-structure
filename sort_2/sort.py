def s_sort(ary):
    for end in range(len(ary) - 1, -1, -1):
        big = end
        for i in range(end):
            if ary[i] > ary[big]:
                big = i
        ary[end], ary[big] = ary[big], ary[end]
    return ary

def i_sort(ary):
    for end in range(1, len(ary)):
        for i in range(end, 0, -1):
            if ary[i] < ary[i - 1]:
                ary[i], ary[i - 1] = ary[i - 1], ary[i]
    return ary

def b_sort(ary):
    for end in range(len(ary) - 1, 0, -1):
        for i in range(end):
            if ary[i] > ary[i + 1]:
                ary[i], ary[i + 1] = ary[i + 1], ary[i]
    return ary

lis = [1, 5, 3, 2, 6, -2]
print(b_sort(lis))