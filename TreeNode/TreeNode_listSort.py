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


def traverse_node(root, result):
    if root == None:
        return
    
    traverse_node(root.right, result)
    result.append(root.data)
    traverse_node(root.left, result)
    return result
    

if __name__ == '__main__':
    import random
    random.seed(0)
    node_array = list(random.randint(0, 5) for _ in range(10) ) 
    result = []
    print(f'임의의 숫자 배열: {node_array}')
    rootNode = generate_tree(node_array) 
    print(f'내림차순 배열: {traverse_node(rootNode, result)}')