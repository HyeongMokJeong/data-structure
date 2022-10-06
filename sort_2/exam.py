num = list(map(str, input().split()))
result = ""
dic = {}

for i in range(len(num)):
    if len(num[i]) == 1:
        num[i] = num[i] * 4
        dic[num[i]] = 1
    else:
        num[i] = num[i] * 2
        dic[num[i]] = 2

num.sort(reverse=True)
for i in num:
    if dic[i] == 1: result += i[0]
    else: result += i[:2]

print(str(int(result)))