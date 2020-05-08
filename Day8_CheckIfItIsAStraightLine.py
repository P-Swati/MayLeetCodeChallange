class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #y=m*x+c
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        if(x1!=x2):
            m=(y1-y2)/(x1-x2)
            c=(y2*x1-y1*x2)/(x1-x2)
            for i in range(2,len(coordinates)): 
                if(coordinates[i][1]!=m*coordinates[i][0]+c): #if values do not satisfy equation
                    return False
            
            return True
        else: #if x coordinates are equal
            for i in range(2,len(coordinates)-1):
                if(coordinates[i][0]!=coordinates[i+1][0]): #then all points should have equal x coordinates
                    return False
                
            return True
