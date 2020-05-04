#create a dict storing all the diamonds (ie chars in J)
#loop over all the characters in S, and check if they are present in J
#if yes then they are jewel, increment count (ans)
#Time Complexity : O(m+n) ==> m=length of J, n=length of S
#Space Complexity : O(m)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        if(not J or not S):
            return 0
        d={}
        
        for i in J:
            d[i]=1
        
        ans=0
        for i in S:
            if(i in d.keys()):
                ans+=1
                
        return ans
