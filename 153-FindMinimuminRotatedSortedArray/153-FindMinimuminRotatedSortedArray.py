// Last updated: 3/17/2025, 12:14:29 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Take two pointers low and high
        low,high = 0 ,len(nums)-1
        ans = float('inf')
        while low<=high:
            # This range is completely sorted
            # low element is smallest element in the range
            if nums[low]<=nums[high]:
                ans = min(ans,nums[low])
                return ans
            mid = (low+high)//2

            # if low element is less than mid element
            # search the right half
            if nums[low]<=nums[mid]:
                ans = min(ans,nums[low])
                low = mid + 1

            # if low element is less than mid element
            # search the right half
            else:
                ans = min(ans,nums[mid])
                high = mid - 1
        return ans
