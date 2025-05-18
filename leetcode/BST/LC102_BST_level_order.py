from collections import deque


def get_level_order(root):
    if not root:
        return []

    q = deque([root])
    tree = []
    while q:
        q_size = len(q)
        level = []
        for _ in range(q_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        tree.append(level)
    return tree
