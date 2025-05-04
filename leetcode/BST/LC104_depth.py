from tree_node import TreeNode

def maxDepth(root):
    if root is None:
        return -1
    l_depth = maxDepth(root.left)
    r_depth = maxDepth(root.right)
    return max(l_depth, r_depth) + 1


def maxDepthIterative(root):
    if root is None:
        return -1
    stack = [(root, -1)]
    res = 0

    while stack:
        node, depth = stack.pop()
        res = max(res, depth)

        if node.left:
            stack.append((node.left, depth + 1))

        if node.right:
            stack.append((node.right, depth + 1))

    return res

