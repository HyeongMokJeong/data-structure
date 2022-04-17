class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for i in range(size)]

def find_vertex(g, vertex):
    stack = []
    visited_ary = []
    current = 0
    stack.append(current)
    visited_ary.append(current)

    while len(stack) != 0:
        next = None
        for i in range(g.SIZE):
            if g.graph[current][i] != 0:
                if i not in visited_ary:
                    next = i
                    break
        if next != None:
            current = next
            stack.append(next)
            visited_ary.append(next)
        else:
            current = stack.pop()
    if vertex in visited_ary:
        return True
    else: return False


def abc(g):
    result1 = 0
    edgeAry = []
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            if g.graph[row][col] == 0:
                continue
            else:
                edgeAry.append([g.graph[row][col], row, col])
    
    from operator import itemgetter
    edgeAry = sorted(edgeAry, key = itemgetter(0), reverse=True)

    newAry = []
    for i in range(0, len(edgeAry)):
        if edgeAry[i][1] > edgeAry[i][2]:
            edgeAry[i][1], edgeAry[i][2] = edgeAry[i][2], edgeAry[i][1]
        if edgeAry[i] in newAry:
            continue
        else:
            newAry.append(edgeAry[i])
    
    index = 0
    while len(newAry) > g.SIZE - 1:
        for i in range(len(newAry)):
            weight = newAry[index][0]
            start = newAry[index][1]
            end = newAry[index][2]

            g.graph[start][end] = 0
            g.graph[end][start] = 0

            if find_vertex(g, start) and find_vertex(g, end):
                del newAry[index]
            else:
                g.graph[start][end] = weight
                g.graph[end][start] = weight
                index += 1
    for i in range(len(newAry)):
        result1 += newAry[i][0]
    return result1


if __name__ == '__main__':
    input_num = int(input())
    g = Graph(input_num)
    input_line = int(input())

    for i in range(input_line):
        weight = input()
        a, b, c = map(int, weight.split())
        g.graph[a-1][b-1] = c
        g.graph[b-1][a-1] = c
    
    print(abc(g))