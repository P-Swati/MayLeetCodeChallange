class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        count1=0
        n=len(nums)
        ans=0
        d[0]=-1
        for i in range(n):
            if(nums[i]==0):
                count1-=1
            else:
                count1+=1
             
            # if(count1==0):
            #     ans=max(ans,i+1)
            
            #if a seen count is seen again, it means there are equal number of ones and zeros between them
            if(count1 in d.keys()):
                ans=max(ans,i-d[count1])
                # d[count1]=i # dont update index to latest, as it will not give larger value of ans
            else: # if not a seen value of count
                d[count1]=i
                
            # print(d)
            # print(ans)
            # print()
                
        return ans
