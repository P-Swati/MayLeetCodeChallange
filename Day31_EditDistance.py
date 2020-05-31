class Solution:
    def rec(self,s1,s2,i,j,states):
        curState=str(i)+'_'+str(j)
        
        if(curState in states.keys()):
            return states[curState]
        
        if(i<0):
            ans = j+1
        elif(j<0):
            ans= i+1
        
        elif(s1[i]==s2[j]):
            ans= self.rec(s1,s2,i-1,j-1,states)
        else:
            ans=1+min(self.rec(s1,s2,i,j-1,states),min(self.rec(s1,s2,i-1,j,states),self.rec(s1,s2,i-1,j-1,states)))
            
        states[curState]=ans
        return ans
        
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        states={}
        return self.rec(word1,word2,len(word1)-1,len(word2)-1,states)
