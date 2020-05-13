#Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
class Solution:
    ans=""
    def rec(self,num,k):
        if(k==0):
            self.ans+=num
            return
        if(k>=len(num)):
            return "0"
        
        minIndex=0
        for idx in range(1,k+1):
            if(num[idx]<num[minIndex]):
                minIndex=idx
                
        self.ans+=num[minIndex]
        
        self.rec(num[minIndex+1:],k-minIndex)
        
    def removeKdigits(self, num: str, k: int) -> str:
        self.rec(num,k)
        
        if(self.ans and self.ans[0]=='0'):
            while(self.ans and self.ans[0]=='0'):
                self.ans=self.ans[1:]
        return self.ans if len(self.ans)>=1 else "0"
