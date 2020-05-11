class Solution:
    def flood(self,image,oldColor,newColor,r,c):
        
        if(r<len(image) and c<len(image[0]) and r>=0 and c>=0 and image[r][c]==oldColor):
            image[r][c] = newColor
            self.flood(image,oldColor,newColor,r+1,c)
            self.flood(image,oldColor,newColor,r-1,c)
            self.flood(image,oldColor,newColor,r,c+1)
            self.flood(image,oldColor,newColor,r,c-1)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if(not image):
            return image
        
        # [[0,0,0],[0,1,1]] max recusrsion depth reached , hence added this case
        if(image[sr][sc]==newColor): # in this case no need of coloring
            return image 
        
        self.flood(image,image[sr][sc],newColor,sr,sc)
        
        return image
