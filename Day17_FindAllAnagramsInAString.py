class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(not s or not p or len(p)>len(s)):
            return []
        
        d={}
        for char in range(ord('a'),ord('z')+1):
            d[chr(char)]=0
        
        for i in p:
            d[i]+=1
                
        i=0
        j=len(p)-1
        
        ans=[]
        d2={}
        
        for char in range(ord('a'),ord('z')+1):
            d2[chr(char)]=0
            
        for k in range(i,j+1):
            d2[s[k]]+=1
            
        if(d2==d):
                ans.append(i)
                    
        while(j+1<len(s)):      
            if(d2[s[i]]>0):
                d2[s[i]]-=1
            
            i+=1
            j+=1
            if(s[j] not in d2.keys()):
                d2[s[j]]=1
            else:
                d2[s[j]]+=1
                
            # print(d2)
                
            if(d==d2):
                ans.append(i)
                
        return ans
        
