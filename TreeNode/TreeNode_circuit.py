class TreeNode:
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None


def generate_tree(sellAry):
    node = TreeNode()
    node.data = sellAry[0]
    root = node

    for i in sellAry[1:]:
        node = TreeNode()
        node.data = i

        current = root
        while True:
            if node.data == current.data:
                break

            if node.data < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
    return root


def preorder(node):
    # 코드 작성 구간: 전위 순회 구현
    if node == None:
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    # 코드 작성 구간: 후위 순회 구현
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = ' ')


def invertTree(root):
    # 코드 작성 구간: 트리 노드들의 위치를 좌우 반전
    # 힌트: 트리의 마지막 leaf 노드부터 반전시키면서 root방향으로 올라가기 (후위 순회)
    if root == None:
        return
    invertTree(root.right)
    invertTree(root.left)
    root.left, root.right = root.right, root.left
    return root

if __name__ == '__main__':
    dataAry = ['바나나맛우유', '츄파춥스', '삼다수', '레쓰비캔커피', '도시락'] 
    rootNode = generate_tree(dataAry)
    print('오늘 판매된 종류(중복X) 트리 전위 순회 --> ', end = ' ')
    preorder(rootNode)
    print('\n오늘 판매된 종류(중복X) 반전 트리 후위 순회 --> ', end = ' ')
    postorder(invertTree(rootNode))