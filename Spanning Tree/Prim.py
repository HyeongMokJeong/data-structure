node = ["A", "B", "C", "D", "E", "F", "G"]
weight = [ [None, 29  , None, None, None, 10  , None],
           [29  , None, 16  , None, None, None, 15  ],
           [None, 16  , None, 12  , None, None, None],
           [None, None, 12  , None, 22  , None, 18  ],
           [None, None, None, 22  , None, 27  , 25  ],
           [10  , None, None, None, 27  , None, None],
           [None, 15  , None, 18  , 25  , None, None]]

def getMinVertex(dist, visited):
    minv = 0
    mind = 9999
    for i in range(1, len(dist)):
        if not visited[i] and mind > dist[i]:
            minv = i
            mind = dist[i]
    return minv

def Prim(node, weight):
    dist = [9999] * len(node)
    dist[0] = 0
    visited = [False for _ in range(len(node))]

    for i in range(len(node)):
        n = getMinVertex(dist, visited) # dist의 idx
        visited[n] = True
        print(node[n], end=": ")

        for j in range(len(node)):
            if weight[n][j] != None:
                if not visited[j] and weight[n][j] < dist[j]:
                    dist[j] = weight[n][j]
        print(dist)
Prim(node, weight)