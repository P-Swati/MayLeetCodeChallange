#approach 1: in dfs, if an edge to a node which is already visited **within cur recursion stack** is encountered, then there is a cycle.

class Solution:
    
    def detectCycle(self,start,adjList,visited):
        visited[start]=1
        
        for i in adjList[start]:
            if(visited[i]==0):
                if(self.detectCycle(i,adjList,visited)==True): # dont use return self.detectCycle(...)
                    return True
            else: # if any neighbour is already visited
                return True
            
        visited[start]=0 #vvi
        
        #here we mark as unvisited because we dont want that this node be seen as visited when
        #we start rec call with other nodes, we only want this as visited within the cur recursion stack
        
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList=collections.defaultdict(list)
        
        for i in prerequisites:
            adjList[i[1]].append(i[0])
            
        # print(adjList)
        visited=[0]*pow(10,5)
        
        ans=False
        for i in range(numCourses):
            # if(visited[i]==0):
            ans= ans or self.detectCycle(i,adjList,visited)
            if(ans==True):
                break
                    
        return not ans
