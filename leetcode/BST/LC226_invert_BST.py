from tree_node import TreeNode


def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    if root.left:
        invertTree(root.left)
    if root.right:
        invertTree(root.right)

    return root
