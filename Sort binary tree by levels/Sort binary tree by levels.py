def tree_by_levels(node):
    if not node:
        return []
    res = []
    queue = []
    queue.append(node)
    while queue:
        now = queue.pop(0)
        res.append(now.value)
        if now.left:
            queue.append(now.left)
        if now.right:
            queue.append(now.right)
    return res
