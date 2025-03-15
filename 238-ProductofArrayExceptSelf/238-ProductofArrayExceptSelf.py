class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # compute suffix product array
        suffix_arr = [1 for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            suffix_arr[i]=suffix_arr[i+1]*nums[i+1]

        # store prefix product in a variable
        prefix_prod  = 1

        #iterate over array and find product of prefix array and suffix array of each element
        for i in range(len(nums)):
            curr_ele  = nums[i]

            # product of suffix array and prefix array
            nums[i] = prefix_prod*suffix_arr[i]

            #update prefix product
            prefix_prod*=curr_ele

        return nums