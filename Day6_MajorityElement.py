class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #boyer moore majority vote algo
        count = 0
        candidate = None

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            if(nums[i]==candidate):
                count+=1
            else:
                count-=1
            

        return candidate
