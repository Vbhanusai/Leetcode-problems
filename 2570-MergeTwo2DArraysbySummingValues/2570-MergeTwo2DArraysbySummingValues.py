class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # brute force using extra space
        i,j=0,0
        n,m = len(nums1),len(nums2)
        result=[]
        while i<n and j<m:
            if nums1[i][0]<nums2[j][0]:
                result.append(nums1[i])
                i+=1
            elif nums1[i][0]>nums2[j][0]:
                result.append(nums2[j])
                j+=1
            else:
                nums1[i][1]+=nums2[j][1]
                result.append(nums1[i])
                i+=1
                j+=1
        if i<n:
            while i<n:
                result.append(nums1[i])
                i+=1
        if j<m:
            while j<m:
                result.append(nums2[j])
                j+=1
        return result