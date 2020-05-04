import math
class Solution:
    #this is the most efficient solution
    # basic intuition:
    # take num=8,9,..,15  number of bits in all these=4
    # num =1000,1001,1010,1011,1100,1101,1110,1111
    # if we exor any of these numbers with a number containing all ones ie 1111, all the bits will automatically be negated 0^1=1, 1^1=0.
    # to get that number with all ones, we take ((2 raiseto 4)-1) ie 1111 (15).
    
    def findComplement(self, num: int) -> int:
        if(num==0):
            return 1
        if(num==1):
            return 0
        
        numBits= (int)(math.log2(num))+1
        
        ans=num^(pow(2,numBits)-1)
            
        return ans
