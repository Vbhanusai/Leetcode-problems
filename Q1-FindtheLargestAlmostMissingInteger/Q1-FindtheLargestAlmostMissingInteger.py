from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        f = Counter(nums)
        if k==1:
            mx=-1
            for x in f:
                if f[x]==1:
                    mx=max(mx,x)
            return mx
        if k==len(nums):
            return max(nums)
        if nums[0]!=nums[-1]:
            if f[nums[0]]==1 and f[nums[-1]]==1:
                return max(nums[0],nums[-1])
            if f[nums[0]]==1:
                return nums[0]
            if f[nums[-1]]==1:
                return nums[-1]
        return -1