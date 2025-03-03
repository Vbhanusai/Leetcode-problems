class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0]*len(nums)
        i,j=0,len(nums)-1
        less,great=0,len(nums)-1
        for i in range(len(nums)):
            if nums[i]<pivot:
                ans[less]=nums[i]
                less+=1
            if nums[j]>pivot:
                ans[great]=nums[j]
                great-=1
            j-=1
        for i in range(less,great+1):
            ans[i]=pivot
        return ans