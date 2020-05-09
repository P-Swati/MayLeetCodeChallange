class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num==0 or num==1):
            return True
        
        i=1
        j=num
        while(i<=j):
            mid=i+(j-i)//2
            if(mid*mid==num):
                return True
            elif(mid*mid<num):
                i=mid+1
            else:
                j=mid-1
                
        return False
