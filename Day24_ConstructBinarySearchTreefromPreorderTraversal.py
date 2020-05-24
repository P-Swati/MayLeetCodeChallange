# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self,nums,i,j):
        # print(i,end=" ")
        # print(j)
        if(i==j): #leaf node
            return TreeNode(nums[i])
        if(j<i): #no insertion
            return None
        
        root=TreeNode(nums[i])
        #find all elements less than current root
        k=i+1
        while(k<len(nums) and nums[k]<nums[i]): #here i missed "k<len(nums)"
            k+=1
        #insert less elements in left subtree
        root.left=self.rec(nums,i+1,k-1)
        #insert remaining in right subtree
        root.right=self.rec(nums,k,j)
        return root
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if(not preorder):
            return None
        if(len(preorder)==1):
            return TreeNode(preorder[0])
        return self.rec(preorder,0,len(preorder)-1)
