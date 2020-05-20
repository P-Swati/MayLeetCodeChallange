class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False
        
        d1={}
        d2={}
        for i in range(ord('a'),ord('z')+1):
            d1[chr(i)]=0
            d2[chr(i)]=0
            
        for i in s1:
            d1[i]+=1
            
        i=0
        j=len(s1)-1
        
        for k in range(i,j+1):
            d2[s2[k]]+=1
            
        # print(d1)
        # print(d2)
        
        if(d2==d1):
            return True
        
        while(j+1<len(s2)):
            if(d2[s2[i]]>0):
                d2[s2[i]]-=1
            i+=1
            j+=1
            d2[s2[j]]+=1
            
            # print(d2)
            if(d2==d1):
                return TruePermutation
