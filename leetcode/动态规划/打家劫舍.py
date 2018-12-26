
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return max(nums)
        dp = [0]*len(nums)
        print(dp)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[len(nums)-1]



if  __name__=='__main__':
    list = [2,7,9,3,1]

    print(Solution().rob(list))