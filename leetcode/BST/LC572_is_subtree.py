from tree_node import TreeNode

def isSameTree(l, r):
    if not l and not r:
        return True

    if not l or not r:
        return False

    if l.val != r.val:
        return False

    return (
            isSameTree(l.left, r.left) and
            isSameTree(l.right, r.right)
    )


def isSubtree(root, subRoot):
    if not subRoot:
        return True

    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return (
            isSubtree(root.left, subRoot) or
            isSubtree(root.right, subRoot)
    )


