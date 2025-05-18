def get_lowest_common_ancestor(root, p, q):
    def helper(node):

        if not node:
            return None

        if node.val == p or node.val == q:
            return node

        left = helper(node.left)
        right = helper(node.right)

        if left and right:
            return node

        return left or right

    ancestor = helper(root)
    return ancestor.val
