class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ## BruteForce
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False

        # # Sorting
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        
        # return False

        # #Set

        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)

        # return False

        #Set length

        return len(set(nums)) < len(nums)

       