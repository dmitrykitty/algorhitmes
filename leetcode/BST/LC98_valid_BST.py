from tree_node import TreeNode

def isValidBST(root):
    if root is None:
        return True

    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        node, min_value, max_value = stack.pop()
        if node.val <= min_value or node.val >= max_value:
            return False

        if node.left:
            stack.append((node.left, min_value, node.val))

        if node.right:
            stack.append((node.right, node.val, max_value))

    return True

def isValidBST2(root):
    def helper(node, min_value, max_value):
        if node is None:
            return True

        if node.val <= min_value or node.val >= max_value:
            return False

        return (
            helper(node.left, min_value, node.val) and
            helper(node.right, node.val, max_value)
        )
    return helper(root, float('-inf'), float('inf'))
