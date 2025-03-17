// Last updated: 3/17/2025, 10:22:17 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize prefix, suffix and ans
        prefix = 1
        suffix = 1
        ans = float('-inf')

        #iterate over nums
        for i in range(len(nums)):

            #if prefix or suffix product is zero don't multiply with further numbers
            if prefix==0:
                prefix = 1
            if suffix==0:
                suffix = 1
            
            #calculate prefix and suffix
            prefix = prefix*nums[i]
            suffix = suffix*nums[len(nums)-1 - i]

            #find max product so far
            ans = max(ans,max(prefix,suffix))
            
        return ans