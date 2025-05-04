from LC104_depth import maxDepth
from tree_node import TreeNode


def isBalanced(root) -> bool:
    if not root:
        return True

    lh = maxDepth(root.left)
    rh = maxDepth(root.right)

    if abs(lh - rh) > 1:
        return False

    return (
            isBalanced(root.left) and
            isBalanced(root.right)
    )
