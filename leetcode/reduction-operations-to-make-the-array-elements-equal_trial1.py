class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operation = 0
        up = 0

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                up +=1
            operation += up
        return operation
