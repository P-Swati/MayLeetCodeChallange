class Solution:
    def countBits(self, num: int) -> List[int]:
        #approach 1: the numbers n and (n&(n-1)), differ by only the least significant bit position
        # eg. 8 -> 1000
        # and 8&7 -> 0000
        #hence we can say : number_of_1's_in_8 = 1 + num_of_1's_in_(8&7)
        
        #approach 2: if we have the number of 1's for the number right shifted by 1 bit, then
        # number_of_ones_in_num = number_of_ones_in_num>>1 + last_bit_of_num (0 or 1)
        # eg. 9== 1001 => ans[1001] = ans[100] + 1 =2
        
        ans=[0]*(num+1)
        
        for i in range(1,num+1):
            # ans[i]=1+ans[i&(i-1)] (1)
            ans[i]=ans[i>>1]+(i&1) #(2)
 
        return ans
