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

# approach 2 : coloring algo : this algo makes sure -
# a) the completely processed nodes are not subjected to be processed again
# b) we can track which nodes are currently under process, and only an edge to nodes being currently processed (visited=1) ( and not those nodes
#    were processed in the past (visited=2)) marks the presence of cycle.

#approach 1: in dfs, if an edge to a node which is already visited **within cur recursion stack** is encountered, then there is a cycle.
# 0:unprocessed
# 1:under processing
# 2:completely processed

class Solution:
    
    def detectCycle(self,start,adjList,visited):
        visited[start]=1
        
        for i in adjList[start]:
            if(visited[i]==0):
                if(self.detectCycle(i,adjList,visited)==True): # dont use return self.detectCycle(...)
                    return True
            elif(visited[i]==1): # if any neighbour is already visited
                return True
            
        visited[start]=2 #vvi
        
        #here we mark as 2 because we dont want that this node be seen as visited when
        #we start rec call with other nodes, we only want this as visited within the cur recursion stack
        # marking as 2 instead as 0 also makes sure that dfs wont be again started at this node
        # as well as this node is not considered as part of currently processing (rec stack) and is previously processed node
        
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList=collections.defaultdict(list)
        
        for i in prerequisites:
            adjList[i[1]].append(i[0])
            
        # print(adjList)
        visited=[0]*pow(10,5)
        
        ans=False
        for i in range(numCourses):
            # print(visited)
            if(visited[i]==0): #only unprocessed nodes will be considered for dfs
                ans= ans or self.detectCycle(i,adjList,visited)
                if(ans==True):
                    break
                    
        return not ans
