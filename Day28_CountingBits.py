class Solution:
    def countBits(self, num: int) -> List[int]:
        #approach: the numbers n and (n&(n-1)), differ by only the least significant bit position
        # eg. 8 -> 1000
        # and 8&7 -> 0000
        #hence we can say : number_of_1's_in_8 = 1 + num_of_1's_in_(8&7)
        
        ans=[0]*(num+1)
        
        for i in range(1,num+1):
            ans[i]=1+ans[i&(i-1)]
            
        return ans
