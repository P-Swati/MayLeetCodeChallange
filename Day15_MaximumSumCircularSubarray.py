class Solution:
    def kadane(self,A):
        localmax=A[0]
        globalmax=A[0]
        
        for i in range(1,len(A)):
            localmax=max(A[i],localmax+A[i])
            globalmax=max(localmax,globalmax)
            
        return globalmax
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if(len(A)==1):
            return A[0]
        
        total=sum(A) # sum of all elements 
        maxSubArraySum=self.kadane(A) # max sum subaarray
        minSubArraySum=-1*self.kadane([-1*A[i] for i in range(len(A))]) # min sum subarray
        # here calculated max subarray sum for negated array, and then negated it, to get min sum
        
        # print(total)
        # print(maxSubArraySum)
        # print(minSubArraySum)
        
        if(total==minSubArraySum): # if sum of array is equal to min subarray sum, it means all elements are negative
            return maxSubArraySum
        
        # otherwise the total- minSubarraySum(most probably negative) will give max,
        # but it should not be less than the max subarray sum
        return max(maxSubArraySum,total-minSubArraySum)
