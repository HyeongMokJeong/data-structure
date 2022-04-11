class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    while start != None:
        print(start.data, end = ' ')
        start= start.link
    
def insertNode(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    else:
        current = head
        while current.link != None:
            pre = current
            current = current.link
            find_flag = False
            if current.data == findData:
                node = Node()
                node.data = insertData
                node.link = current
                pre.link = node
                find_flag = True
                return
        if not find_flag:
            node = Node()
            node.data = insertData
            current.link = node
            return

def deleteNode(deleteData):
    global memory, head, current, pre
    current = head
    if head.data == deleteData:
        head = head.link
        del current
        return

    else:
        while current.link != None:
            pre = current
            current = current.link
            delete_flag = False
            if current.data == deleteData:
                pre.link = current.link
                del current
                delete_flag = True
                return
        if not delete_flag:
            print("없습니다.")
            return



memory = []
head, current, pre = None, None, None
dataArray = ["파이썬", "C++", "MATLAB"]

node = Node()	
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:	
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

print('## 초기 연결 리스트 ##')
printNodes(head)

print('\n## 파이썬 위치에 R 추가 결과(첫번째 노드 삽입) ##')
insertNode("파이썬", "R")
printNodes(head)

print('\n## C++ 위치에 C 추가 결과(중간 노드 삽입) ##')
insertNode("C++", "C")
printNodes(head)

print('\n## MATLAB 위치에 JAVA 추가 결과(마지막 노드 삽입) ##')
insertNode("MATLA", "JAVA")
printNodes(head)

print("\n# c 삭제")
deleteNode("C")
printNodes(head)