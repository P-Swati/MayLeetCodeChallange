class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # equivalent to longest common subsequence
        
        dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        
        for i in range(len(A)):
            for j in range(len(B)):
                if(i==0 or j==0):
                    pass
                if(A[i]==B[j]):
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
                    
        return dp[len(A)][len(B)]
