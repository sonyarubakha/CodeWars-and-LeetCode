# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    '''
    a binary tree node class.
    '''

    def __init__(self, val=0, left=None, right=None):
        '''
        initializes a binary tree node.
        '''
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Solution class for task.
    '''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        deletes the node with the given key in the BST
        '''
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            now = root.right
            while now.left:
                now = now.left
            root.val = now.val
            root.right = self.deleteNode(root.right, root.val)
        return root
