class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i==0 or j==0):
                    dp[i][j]=matrix[i][j]
                else:
                    if(matrix[i][j]==1):
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                        
                ans+=dp[i][j]
                
        for i in matrix:
            print(i)
        print()
        for i in dp:
            print(i)
                
        return ans
