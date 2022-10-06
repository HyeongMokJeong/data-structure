A = [4, 16, 15, 8, 7, 13, 14, 2, 5]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def max_heaplfy(ary):
    for j in range(1, len(ary)):
        for i in range(1, len(ary)):
            tmp = i
            if (i % 2 == 0): tmp -= 1
            if (ary[tmp // 2] < ary[i]):
                if (ary[i - 1] > ary[i]): ary[i - 1], ary[tmp // 2] = ary[tmp // 2], ary[i - 1]
                else: ary[i], ary[tmp // 2] = ary[tmp // 2], ary[i]
    return ary

print(max_heaplfy(B))