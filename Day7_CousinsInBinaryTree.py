# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #function to find pointer to a node and its parent , along with depth , returns a tuple (pointer, parentPointer, depth)
    
    def find(self,root,parent,depth,val):
        if(not root):
            return None
        elif(root.val==val):
            return (root,parent,depth)
        else:
            return self.find(root.left,root,depth+1,val) or self.find(root.right,root,depth+1,val)
            
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xPtr=self.find(root,None,0,x)
        yPtr=self.find(root,None,0,y)
        # print(xPtr)
        # print(yPtr)
        
        #if parents are different and depths are same
        if(xPtr!=None and yPtr!=None and xPtr[1]!=yPtr[1] and xPtr[2]==yPtr[2]):
            return True
        return False
