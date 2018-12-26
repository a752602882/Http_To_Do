class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i=0
        n = len(nums)
        while i<n:
            b = target-nums[i]
            if b in nums:
                j=nums.index(b)
                if i!=j:
                   return i,j
            i+=1



if __name__ == '__main__':
    nums = [3,2,4]
    target = 6

    print(Solution().twoSum(nums, target))
