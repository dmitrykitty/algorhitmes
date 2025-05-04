from tree_node import TreeNode

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    current = root
    while current:
        if val < current.val:
            if current.left:
                current = current.left
            else:
                current.left = TreeNode(val)
                return root
        else:
            if current.right:
                current = current.right
            else:
                current.right = TreeNode(val)
                return root

    return root

def insertIntoBST2(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST2(root.left, val)
    else:
        root.right = insertIntoBST2(root.right, val)

    return root