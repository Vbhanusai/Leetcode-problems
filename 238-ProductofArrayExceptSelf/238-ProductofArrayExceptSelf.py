class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)
            p = 1
            zero_count = 0
            out = [0] * n

            for i in nums:
                if(i != 0): p *= i
                else: zero_count += 1

            if zero_count > 1: return out

            for i in range(n):
                if (zero_count > 0 and nums[i] != 0): out[i] = 0
                elif(zero_count > 0 and nums[i] == 0): out[i] = p
                else: out[i] = p//nums[i]

            return out
        