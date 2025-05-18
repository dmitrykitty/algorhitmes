def has_path_sum(root, target: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    return (
            has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val)
    )

