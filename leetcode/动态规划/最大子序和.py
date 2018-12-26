class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        MaxSum = nums[0]
        if len(nums)==1 and nums[0]<0:
            return nums[0]

        for i in range(len(nums)):
            sum += nums[i]
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0 :
                sum = 0
        return MaxSum
