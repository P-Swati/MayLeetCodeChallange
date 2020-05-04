# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this can be solved using binary search approach
        # g g g g b b b b b b ==> all goods followed by bads
        # need to find the first bad
        
        lo=1
        hi=n
        
        while(lo<hi):
            mid=lo+(hi-lo)//2
            if(isBadVersion(mid)):
                hi=mid
            else:
                lo=mid+1
                
        return lo
