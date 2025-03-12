class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hash set to store unique values
        hash  = set()

        #iterate over 'nums' array
        for x in nums:
            
            # if current element is present in hash return True
            if x in hash:
                return True

            # add element to the hash set
            hash.add(x)

        # return false if every element is unique
        return False

        