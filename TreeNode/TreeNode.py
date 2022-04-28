from dataclasses import dataclass
from turtle import left


class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    
def makeTree(list):
    node = TreeNode()
    node.data = list[0]
    root = node

    for i in list[1:]:
        node = TreeNode()
        node.data = i

        current = root
        while True:
            if i == current.data:
                break

            if i < current.data:
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

def printTree(root):
    if root == None:
        return
    print(root.data , end=' ')
    printTree(root.left)
    printTree(root.right)

list = [1, 40, 5, 3, 4, 5, 6]
root = makeTree(list)