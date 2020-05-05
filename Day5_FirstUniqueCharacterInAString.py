class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if(i not in d.keys()):
                d[i]=1
            else:
                d[i]+=1
                
        for i in range(len(s)):
            if(d[s[i]]==1 ): #if any character has freq=1, return its index
                return i
            
        return -1 #if no such character found return -1
