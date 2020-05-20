# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#approach:
# perform an inorder traversal over the bst, an inorder traversal always gives numbers in sorted order in case 
# of bst. as soon as we complete traversing k elements, return the kth element
class Solution:
    count=0
    def inorder(self,root,k):
        if(root):
            a=self.inorder(root.left,k)
            if(a is not None): #if kth min returned from left subtree
                return a
            
            self.count+=1 
            if(self.count==k): #else check if k traversed, if yes then return this
                return root.val
            
            b=self.inorder(root.right,k)
            if(b is not None):
                return b
            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if(not root):
            pass
        return self.inorder(root,k)
