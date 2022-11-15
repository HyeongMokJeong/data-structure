node = ["A", "B", "C", "D", "E", "F", "G"]
weight = [(0, 1, 29), (2, 3, 7), (1, 5, 34), (2, 3, 3), (1, 2, 35), (4, 5, 53), (0, 4, 75), (5, 6, 25), (3, 5, 23), (3, 6, 13), (2, 3, 30)]
weight.sort(key=lambda x:x[2])
union_table = [i for i in range(len(node))]
count = 0

for i in weight:
    if (union_table[i[0]] != union_table[i[1]]):
        for j in range(len(union_table)):
            if (union_table[j] == union_table[i[1]]): union_table[j] = union_table[i[0]]
        print(f"간선 추가 : ({node[i[0]]}, {node[i[1]]}, {i[2]})")
        count += 1
        if (count >= len(node) - 1): break