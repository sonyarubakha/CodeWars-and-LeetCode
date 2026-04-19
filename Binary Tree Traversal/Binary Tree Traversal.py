# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    res = [node.data]
    left_res = pre_order(node.left)
    right_res = pre_order(node.right)
    return res + left_res + right_res

# In-order traversal
def in_order(node):
    if not node:
        return []
    res = [node.data]
    left_res = in_order(node.left)
    right_res = in_order(node.right)
    return left_res + res + right_res


# Post-order traversal
def post_order(node):
    if not node:
        return []
    res = [node.data]
    left_res = post_order(node.left)
    right_res = post_order(node.right)
    return left_res + right_res + res
