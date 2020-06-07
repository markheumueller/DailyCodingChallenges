class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'[Node]: {self.val} - Left: {self.left} - Right: {self.right}'


def serialize(node: Node) -> str:
    if not node:
        return ""
    left = serialize(node.left)
    right = serialize(node.right)
    return f'{str(node.val)}+{left}+{right}'


def deserialize(node: str) -> Node:
    data, left, right = node.split("+", 2)

    node = Node(data)
    node.left = deserialize(left)
    node.right = deserialize(right)

    return node
