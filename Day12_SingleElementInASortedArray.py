class Solution:
    # All elements before the required have first occurrence at even index (0, 2, ..) and next occurrence at odd index (1, 3, …). 
    # And all elements after the required element have first occurrence at odd index and next occurrence at even index.
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        i=0
        j=len(nums)-1
        
        while(i<=j):
            mid=i+(j-i)//2
            if(mid%2==0):
                if(mid+1<len(nums) and nums[mid]==nums[mid+1]): # this even index has 1st occurence of some ele (ideal)
                    i=mid+2 # req num is after it
                elif(mid-1>=0 and nums[mid]==nums[mid-1]):  # this even index has 2nd occurence of some ele
                    j=mid-2
                else: # not equal to any of its adjacents
                    return nums[mid]
                    
            else:
                if(mid-1>=0 and nums[mid]==nums[mid-1]): # this odd index has 2nd occurence of some ele (ideal)
                    i=mid+1 # req num is after it
                elif(mid+1<len(nums) and nums[mid]==nums[mid+1]): # this odd index has 1st occurence of some ele
                    j=mid-1
                else: # not equal to any of its adjacents
                    return nums[mid]
                    
        return -1
