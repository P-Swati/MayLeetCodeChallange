class Solution:
    # approach : calc dist of each point from origin , make tuple (dist ,(x,y))
    # use max heap approach to get k closest points (like k smallest items)
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if(K==len(points)):
            return points
        
        points2=[]
        for i in range(len(points)):
            points2.append(( -1*(pow(points[i][0],2)+pow(points[i][1],2)) , points[i] ) )
            
        print(points2)
        
        heap=[]
        
        for i in range(K):
            heap.append(points2[i])
            
        heapq.heapify(heap)
            
        # print(heap)
        
        for i in range(K,len(points2)):
            top=abs(heap[0][0])
            if(top>abs(points2[i][0])):
                heapq.heappop(heap)
                heapq.heappush(heap,points2[i])
                
        # print(heap)
        
        ans=[]
        
        while(heap):
            ans.append(heapq.heappop(heap)[1])
            
        return ans
        
