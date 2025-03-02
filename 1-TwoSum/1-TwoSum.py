class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,x in enumerate(nums):
            if target-x in hash:
                return [hash[target-x],i]
            hash[x]=i
        return
        