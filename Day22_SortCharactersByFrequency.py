class Solution:
    #approach :
    # store in heap the tuple (frequency,character).
    # this way the heap orders it first acc to freq, then acc to the character
    # the ordering acc to the character makes sure that same characters with equal freq should be
    # grouped together
    def frequencySort(self, s: str) -> str:
        
        d={}
        
        for i in s:
            if(i not in d.keys()):
                d[i]=1
            else:
                d[i]+=1
         
        l=[]
        heapq.heapify(l)
        
        for i in range(len(s)):
            heapq.heappush(l,((d[s[i]],s[i])))
            
        # print(l)
        
        ans=''
        while(l):
            ans+=heapq.heappop(l)[1]
            
        return ans[::-1] # reverse beacuse we were using a min heap
