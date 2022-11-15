A = [1, 3, 5, 3, 4, 2, 5, 1, 2, 3, 4, 2, 5, 3, 2, 4, 1, 5]
result = []
dic = {i : 0 for i in range(1, 6)}

for i in A: dic[i] += 1

for i in list(dic.keys()):
    for _ in range(dic[i]):
        result.append(i)

# 최빈값
max_count = max(dic.values());
max_list = [key[0] for key in dic.items() if key[1] == max_count]

print(f"최빈값 : {max_list[0] if len(max_list) == 1 else max_list[1]}")

print(result)