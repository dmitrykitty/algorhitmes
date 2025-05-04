from tree_node import TreeNode

def searchBST(root, target):
    if not root:
        return None
    if root.val == target:
        return root

    if target < root.val:
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target)

