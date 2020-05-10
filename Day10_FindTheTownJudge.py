class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if(N==1):
            return 1
        if(not trust):
            return -1
        if(len(trust)==1):
            return trust[0][1]
        
        d={}
        trustList={} #persons who trust this person
        
        for i in range(1,N+1):
            d[i]=-1
            trustList[i]=0
            
        for i in trust: 
            d[i[0]]=1 # all persons who trust someone
            trustList[i[1]]+=1
            
        # print(d)
        # print(trustList)
            
        for i in d.keys():
            if(d[i]==-1): # the person who trusts no one
                if(trustList[i]==N-1): # if N-1 people trust that person
                    return i
        
            
        return -1
