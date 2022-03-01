import sys

sys.setrecursionlimit(10000)


class Node(object):
    def __init__(self, data: list):
        self.data = data
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data: list):
        if self.root is None:
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if data[1][0] < current_node.data[1][0]:  # 현재 노드의 왼쪽에 들어가야할 때
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(data)
                        break
                else:  # 현재 노드의 오른쪽에 들어가야할 때
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(data)
                        break


pre_ret = []
post_ret = []


def preorder(root: Node):
    pre_ret.append(root.data[0])
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)


def postorder(root: Node):
    if root.left is not None:
        postorder(root.left)
    if root.right is not None:
        postorder(root.right)
    post_ret.append(root.data[0])


def solution(nodeinfo):
    answer = [[]]
    for i, node in enumerate(nodeinfo):
        nodeinfo[i] = [i + 1, node]
    nodeinfo.sort(key=lambda x: (-x[1][1], x[1][0]))  # 1-y축 기준 내림 차순, 2-x축 기준 오름 차순
    tree = BinaryTree()
    for node in nodeinfo:
        tree.insert(node)
    preorder(tree.root)
    postorder(tree.root)
    answer = [pre_ret] + [post_ret]
    print(answer)
    return answer


if __name__ == '__main__':
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
