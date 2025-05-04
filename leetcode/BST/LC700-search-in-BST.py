class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, target):
    if not root:
        return None
    if root.val == target:
        return root

    if target < root.val:
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target)