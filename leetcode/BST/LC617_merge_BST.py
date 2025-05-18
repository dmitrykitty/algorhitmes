from tree_node import TreeNode


def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None

    if not root1 or not root2:
        return root1 if root1 else root2

    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1

def mergeTreesIter(root1, root2):
    if not root1 and not root2:
        return None
    if not root1 or not root2:
        return root1 if root1 else root2
