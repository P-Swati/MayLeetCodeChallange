class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if(not A or not B):
            return []
        
        #sort the intervals acc to start of each interval
        A.sort(key=lambda x : x[0])
        B.sort(key=lambda x : x[0])
        
        ans=[]
        for i in range(len(A)):
            j=0
            # continue only while start of second interval is less than end of first interval,if this is false 
            # there is no possibility of intersection
            while(j<len(B) and B[j][0]<=A[i][1]):
                #now intersection exists only when end of second interval is greater than start
                # of first interval, otherwise they are disjoint
                if(B[j][1]>=A[i][0]):
                    temp=[max(A[i][0],B[j][0]),min(A[i][1],B[j][1])] #merged interval is (max of start points, min of end points)
                    ans.append(temp)
                    
                j+=1
                
        return ans
