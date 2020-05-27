class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        #make adjList
        
        adjList=collections.defaultdict(list)
        
        for i in dislikes:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
            
        print(adjList)
        
        queue=deque()
        
        visited=[0]*N
        assignedGroup={}
        
        for i in range(1,N+1): # need to add a for loop beacuse the graph might be present as 
            # disjoint components
            if(visited[i-1]==0): # if node has already been visited, no need to explore again
                #else do a bfs considering this node as start node
                queue.append(i)
                visited[i-1]=1
                assignedGroup[i]=0 # first group

                while(queue):
                    pop=queue.popleft()

                    for j in adjList[pop]:
                        # if color to be assigned is opp to the color that was already assigned => conflict
                        if(j in assignedGroup.keys() and assignedGroup[j]!=int(not assignedGroup[pop])):
                            return False
                        
                        if(visited[j-1]==0): # need to check if the neighbour is already visited, this is because
                            # of undirected edges and adjList has adj[1]=2 and adj[2]=1 for one edge (1,2).
                            #ie two entries for each edge
                            queue.append(j)
                            visited[j-1]=1
                            assignedGroup[j]=int(not assignedGroup[pop]) # assign opp group to neighbours
                    
        return True
                    
